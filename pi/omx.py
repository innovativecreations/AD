import os
import subprocess
files = os.listdir("vid")
print(files)


def play_video(video_path):
    # Construct the command to launch mpv in full-screen mode
    command = ['mpv', '--fs', video_path]

    # Launch mpv in a subprocess
    subprocess.call(command)

# Specify the path to your video file
video_path = 'vid/The_Good_Move_for_People.mp4'

# Play the video in full-screen mode
while True:
# Iterate over video paths
    for vid in files:
        # Load the video file
        video_path = "vid/" + vid
        play_video(video_path)