import subprocess

output_file_path = "output.mp4"

# Updated ffmpeg command with smaller video size and reduced bitrates
command = [
    "ffmpeg",
    "-f", "v4l2",
    "-video_size", "320x240",  # Setting a smaller video size
    "-i", "/dev/video0",
    "-f", "alsa",
    "-i", "default",
    "-c:v", "libx264",
    "-profile:v", "baseline",  # Use the baseline profile for wider compatibility
    "-level", "3.0",  # Use level 3.0 for compatibility with older devices
    "-preset", "ultrafast",
    "-b:v", "300k",  # Reduced video bitrate to 300 kbps
    "-pix_fmt", "yuv420p",  # Use the yuv420p pixel format for wider compatibility
    "-c:a", "aac",
    "-b:a", "64k",  # Reduced audio bitrate to 64 kbps
    "-strict", "experimental",
    "-t", "300",  # Five minutes (300 seconds)
    "-vf", "transpose=1,transpose=1",  # Rotate the video 180 degrees clockwise (transpose=1) twice
    "-movflags", "+faststart",  # Optimize for web playback
    output_file_path
]

# Run the command
subprocess.run(command)
