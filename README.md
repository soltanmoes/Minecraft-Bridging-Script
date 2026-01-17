# Minecraft Bridging Script

An automated bridging bot for Minecraft that detects when you're at the edge of a block and automatically performs the bridging action (crouch, release, place block).

## Disclaimer

This script is for educational purposes only. Using automation tools in multiplayer servers may violate server rules and could result in bans. Use at your own risk and only in single-player or on servers that allow such tools.

## Features

- Automatic edge detection
- Automatic block placement
- Easy exit with ESC key

## Requirements

- Python 3.7 or higher
- Opencv among other libraries
- Minecraft (Java Edition)
- Windows OS

## Installation

1. Clone or download this repository
2. Install required dependencies:

pip install keyboard pyautogui opencv-python pillow numpy

## Troubleshooting

- You might need to adjust parameters (bbox) if your screen is of a different resolution (I'm on 1440p)
- Check the config, I use ctrl to crouch