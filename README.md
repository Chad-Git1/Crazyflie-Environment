# Crazyflie-Environment

This Repository is the home the core simulation environment for the first portion of the Honours Project for Chad Yassin, Pronoy Fuad, and Kevin Naveen, and also for the Honours Project of Michael O'Sullivan.

# Setup

Install dependencies with `pip install -r requirements.txt`

# Running

Currently, we can run a test with `main.py` (temporary, main.py will change)
- On Windows and Linux, you can use `python main.py`
- On macOS, you can use `mjpython main.py` due to how MuJoCo sets up the OpenGL context
  - mjpython installs as part of MuJoCo and wraps your system python version