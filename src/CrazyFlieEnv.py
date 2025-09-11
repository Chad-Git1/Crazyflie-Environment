import gymnasium as gym
from gymnasium import spaces
import numpy as np
import mujoco

class CrazyflieEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(self, xml_path):
        super().__init__()

        # MuJoCo model
        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data = mujoco.MjData(self.model)

        # Observations for hover task: 13 dimensions, see get_obs()
        obs_high = np.inf * np.ones(13, dtype=np.float32)
        self.observation_space = spaces.Box(-obs_high, obs_high, dtype=np.float32)

        # Action space: 4 dimensions (for now only using the thrust in step()) 
        # thrust + rotation axes (roll, pitch, yaw)
        # Rotation axes: https://en.wikipedia.org/wiki/Aircraft_principal_axes
        act_high = np.array([0.1, 1, 1, 1], dtype=np.float32)
        act_low = np.array([-0.1, -1, -1, -1], dtype=np.float32)
        self.action_space = spaces.Box(act_low, act_high, dtype=np.float32)

        # Rendering viewer
        self.viewer = None

        # Target height
        self.target_height = 0.5


    def reset(self):
        super().reset()

        # Reset simulation
        mujoco.mj_resetData(self.model, self.data)

        # Random initial z around 0.1–0.2 m
        self.data.qpos[2] = 0.1 + 0.1 * np.random.rand()
        self.data.qvel[:] = 0.0

        return self._get_obs(), {}


    # Combines base hover (e.g. see hover_test.py) with RL actions
    def step(self, action):
        # Clip action within action space
        action = np.clip(action, self.action_space.low, self.action_space.high)

        # Simple PD hover control (ignoring orientation for now)
        BASE_THRUST = 0.26487
        kp = 0.3
        kd = 0.1

        z_position = self.data.qpos[2]
        z_velocity = self.data.qvel[2]

        p_error = self.target_height - z_position
        d_error = -z_velocity

        # Combine RL action (only thrust part) with PD hover control
        thrust = BASE_THRUST + kp * p_error + kd * d_error + action[0]

        # Apply thrust control (no orientation)
        self.data.ctrl[:] = np.array([thrust, 0.0, 0.0, 0.0])

        # Take a step, track observations
        mujoco.mj_step(self.model, self.data)
        obs = self._get_obs()

        # Reward is negative distance to target height
        reward = -abs(self.target_height - z_position)

        # Episode ends if Crazyflie falls below 0
        done = bool(z_position < 0.0)

        return obs, reward, done, False, {}


    def _get_obs(self):
        # Observation: position[x, y, z], orientation[qz, qy, qz, q2], velocity[vx, vy, vz], angular velocity[wx, wy, wz]
        pos = self.data.qpos[:3]
        quat = self.data.qpos[3:7]
        vel = self.data.qvel[:3]
        ang_vel = self.data.qvel[3:6]

        return np.concatenate([pos, quat, vel, ang_vel]).astype(np.float32)


    def render(self):
        if self.viewer is None:
            self.viewer = mujoco.viewer.launch_passive(self.model, self.data)
        self.viewer.sync()


    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None
