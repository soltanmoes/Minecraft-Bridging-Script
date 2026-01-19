# Minecraft Bridging Script

An automated bridging bot for Minecraft that detects when you're at the edge of a block and automatically performs the bridging action (crouch, place block, release crouch).

## Disclaimer

This script is for educational purposes only. Using automation tools in multiplayer servers may violate server rules and could result in bans. Use at your own risk and only in single-player or on servers that allow such tools.

## Features

- Automatic edge detection using player position tracking
- Automatic block placement
- Hold Alt to activate, release Alt to stop
- Works with Minecraft's native API through Minescript mod
- Detects movement direction automatically

## Requirements

- **Minecraft Java Edition** (1.19+ recommended)
- **Python 3.7 or higher**
- Minescript Python package -- Check their website for Documentation

## Installation

1. **Install Minescript Mod:**
   - Download the Minescript mod for your Minecraft version
   - Install it using a mod loader
   - Launch Minecraft with the mod installed

2. **Set up the script:**
   - Clone or download this repository
   - Place `bridging.py` in your Minescript scripts directory
   - The script will be accessible through the Minescript interface in-game

## Usage

1. **Start Minecraft** with the Minescript mod loaded
2. **Open the Minescript interface** and run `bridging.py`
3. **Position yourself** at the start of where you want to bridge
4. **Look at the side of a block** (not up or down) to set the direction
5. **Press and hold Alt** to start bridging
6. **Walk backwards** - the bot will automatically:
   - Detect when you reach the edge
   - Hold sneak (crouch)
   - Place a block
   - Release sneak
7. **Release Alt** to stop the script

## How It Works

The script uses the Minescript API to:
1. Track your player position in real-time
2. Detect when you move to the edge of a block (position changes by 1 block)
3. Automatically perform the bridging sequence:
   - Hold sneak (crouch)
   - Wait for valid block placement target
   - Place block (use item)
   - Release sneak
4. Continue until you release the Alt key

## Configuration

The script uses:
- **Alt key** (Left Alt) - Hold to activate, release to stop
- **Sneak key** - Uses your Minecraft sneak key binding
- **Use key** - Uses your Minecraft use key binding (right-click by default)

## Troubleshooting

- **Script doesn't start**: Make sure Minescript mod is properly installed and loaded
- **Wrong direction**: Make sure you're looking at the side of a block (not up/down) when you start
- **Blocks not placing**: Check that you have blocks in your hotbar and are holding the correct item
- **Script stops unexpectedly**: I know and I am working on it.

## Notes

- The script automatically detects which direction you're bridging (north/south/east/west)
- It only places blocks when you're at the edge and have a valid target

## License

This project is provided as-is for **educational purposes**.