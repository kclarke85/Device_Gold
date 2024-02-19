import subprocess
import pygame.mixer as mixer

def play_mp3(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        continue

def say_message(message):
    subprocess.run(["espeak", "-ven+f3", f'"{message}"'])

if __name__ == "__main__":
    path_to_mp3 = "transmit.mp3"  # Replace with the path to your MP3 file
    message = "A potential negative encounter is underway. The device owner's family has been alerted."

    play_mp3(path_to_mp3)
    say_message(message)
    subprocess.run(["python", "camvid_out.py"])
    subprocess.run(["python", "Send_SMS_Alert.py"])


