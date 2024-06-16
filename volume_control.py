#!/usr/bin/env python3

import subprocess
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item
import time
import threading

# Function to create an icon image
def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image

# Function to open pavucontrol on the Playback tab
def open_pavucontrol():
    def open_and_focus():
        # Open pavucontrol
        subprocess.Popen(['pavucontrol'])
        # Wait for pavucontrol to start
        time.sleep(1)
        # Use xdotool to focus on the Playback tab
        subprocess.run(['xdotool', 'search', '--class', 'pavucontrol', 'windowactivate', '--sync', 'key', 'ctrl+2'])
    
    # Run in a separate thread to avoid blocking the icon
    threading.Thread(target=open_and_focus).start()

# Function to exit the program
def exit_action(icon, item):
    icon.stop()

# Create an image for the system tray icon
icon_image = create_image(64, 64, 'black', 'white')

# Define the menu for the system tray icon
menu = (item('Open Volume Control', open_pavucontrol), item('Exit', exit_action))

# Create the system tray icon
icon = pystray.Icon('volume_control', icon_image, 'Volume Control', menu)

# Run the system tray icon
icon.run()
