# asteroids

Asteroids is my second [Boot.dev](https://www.boot.dev) project!

It's a simple clone of the classic [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)) game.

## How to Run

### Windows
Download the [game.exe](https://github.com/phnthnhnm/asteroids/releases/latest/download/game.exe) file in the [release](https://github.com/phnthnhnm/asteroids/releases/latest)

### Other Platforms

1. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## How to Play

- Use `W`, `A`, `S`, `D` keys to move your spaceship.
- Press `Space` to shoot.
- Press `Q` to switch weapon types.
  
## Extended Features

My project has been extended beyond what was required in the original challenge:
- Added a scoring system
- Implemented multiple lives and respawning
- Added an explosion effect for the asteroids
- Added acceleration to the player movement
- Made the objects wrap around the screen instead of disappearing
- Added a background image
- Created different weapon types
