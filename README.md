# Asteroids Game

A classic Asteroids arcade game built with Python and Pygame.

## Features

- **Timer**: Track your survival time
- **Scoring System**: Earn points by destroying asteroids
  - Small asteroids: 100 points
  - Medium asteroids: 50 points
  - Large asteroids: 25 points
- **Cross-Device Support**: 
  - Resizable window for different screen sizes
  - Fullscreen mode toggle
  - Screen wrapping for smooth gameplay

## Controls

- **W/A/S/D**: Move and rotate the spaceship
- **SPACE**: Shoot
- **F**: Toggle fullscreen mode

## Installation

1. Make sure you have Python 3 installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

```bash
python main.py
```

## Game Rules

- Destroy asteroids by shooting them
- Larger asteroids split into smaller ones when hit
- Avoid colliding with asteroids
- Your score and survival time are displayed on screen
- Game ends when you collide with an asteroid
