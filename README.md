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
