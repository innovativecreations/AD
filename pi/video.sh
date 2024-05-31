#!/bin/bash
# Play all video files in a loop from a specified directory
relativePath = "/home/mayank/Desktop/AD/pi/"
DIRECTORY=relativePath + 'vid'
# Ensures the display variable is set
export DISPLAY=:0

while true; do
  # Use VLC to play the videos in a loop
  vlc --fullscreen --loop --no-video-title-show "$DIRECTORY"/*
  sleep 10 # Wait for 10 seconds before restarting the loop
done
