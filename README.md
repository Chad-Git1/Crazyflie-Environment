# Crazyflie-Environment

This Repository is the home the core simulation environment for the first portion of the Honours Project for Chad Yassin, Pronoy Fuad, and Kevin Naveen, and also for the Honours Project of Michael O'Sullivan and Aydin Y.

# Setup

Install dependencies with `pip install -r requirements.txt`

# Running the main training + evaluation (visualization) file

Training and final simulation done in `main.py`
- On Windows and Linux, you can use `python main.py`
- On macOS, you can use `mjpython main.py` due to how MuJoCo sets up the OpenGL context
  - mjpython installs as part of MuJoCo and wraps your system python version

# Running tests (e.g. basic hovering)

Tests are under `.../src/Tests`
- On Windows and Linux, you can use `python <TEST>.py`
- On macOS, you can use `mjpython <TEST>.py`

# Environment and Training

Simulation & Physics Engine: **[MuJoCo](https://mujoco.org/)**
- Handles all physical dynamics of the Crazyflie drone
- Provides 3D simulation including forces, torques, collisions, and drone kinematics
- Real-time visualization with the mujoco viewer

Environment Definition: **[Gymnasium API](https://gymnasium.farama.org/index.html)**
- Wraps the MuJoCo model into a reinforcement learning environment
  - Observation space (drone position, orientation, linear velocities, and angular velocities)
  - Action space (thrust and rotation)
  - Stepping: action --> simulation step --> calculate reward --> check termination

Reinforcement Learning Algorithms
- FILL IN LATER - not sure if this stuff should be done in individual lab repos (e.g. our group repos in the mirl-lab org on GitHub)
