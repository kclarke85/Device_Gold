#import assemblyai as aai
# import subprocess
# import sounddevice as sd
# import numpy as np
# import os
# import wave
# import json
# from pymongo import MongoClient
# 
# # Replace with your AssemblyAI API key
# aai.settings.api_key = "523057ab8c494c6ba1d31121c46dc99a"
# 
# # MongoDB configuration
# mongo_client = MongoClient(
#     'mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc')  # Update with your MongoDB connection string
# db = mongo_client.webapp_subscriptions
# all_words_phrases_collection = db.all_words_phrases
# 
# # Set the microphone parameters
# sample_rate = 44100  # Adjust based on your microphone's sample rate
# duration = 10 # Set the duration for audio capture in seconds
# 
# # Load local phrases from the attached JSON content and create a dictionary
# json_content = {
#     "phrases": [
#         "Encounter home",
#         "Encounter Go Go.",
#         "Step out of the car.",
#         "This is ridiculous.",
#         "I know my rights.",
#         "You can't do this.",
#         "I didn't do anything wrong.",
#         "I wasn't speeding.",
#         "This is unfair.",
#         "Why did you pull me over?.",
#         "You have no right to stop me.",
#         "I don't have to show you my ID.",
#         "I won't step out of the vehicle.",
#         "You're just targeting me.",
#         "This is discrimination.",
#         "I want to speak to your supervisor.",
#         "Get someone higher up here.",
#         "This is ridiculous!.",
#         "I can't believe this is happening.",
#         "I know my rights!.",
#         "You can't do this to me.",
#         "What's going to happen now?.",
#         "I need to get to.",
#         "I know the law better than you do.",
#         "I'm running late.",
#         "I didn't see the speed limit sign.",
#         "I had an emergency.",
#         "Why are you hassling me?.",
#         "You're just out to get people.",
#         "This is an abuse of power.",
#         "You're making things up.",
#         "I don't have to answer your questions.",
#         "I'm not doing anything you say.",
#         "I don't trust cops.",
#         "You're just trying to trick me.",
#         "This is ridiculous.",
#         "I can't believe I'm being pulled over.",
#         "Just give me the ticket and let me go.",
#         "Hurry up and finish this.",
#         "I shouldn't be dealing with this.",
#         "This is a waste of my time.",
#         "Victim Mentality:.",
#         "Why is everyone always picking on me?.",
#         "I never catch a break.",
#         "I'm not a criminal.",
#         "I'm not a threat.",
#         "Other people were driving faster than me.",
#         "You're all just trying to meet a quota.",
#         "This is a setup.",
#         "Can we get this over with?.",
#         "I have places to be.",
#         "Why are you bothering me?.",
#         "Don't you have anything better to do?.",
#         "Explain why you pulled me over.",
#         "Tell me exactly what I did wrong.",
#         "This is an outrage!.",
#         "You're ruining my day.",
#         "I don't believe I was speeding.",
#         "Are you sure about this?.",
#         "Cops are just power-hungry.",
#         "I've never been pulled over before.",
#         "I can't believe this is happening to me.",
#         "Can't you let me off with a warning?.",
#         "I promise it won't happen again.",
#         "Just my luck.",
#         "This is a joke.",
#         "I don't have time for this.",
#         "Why do these things always happen to me?.",
#         "I'm having the worst day."
#     ]
# }
# 
# local_phrases_dict = {phrase: True for phrase in json_content["phrases"]}
# 
# 
# def record_audio():
#     print("Recording audio. Speak now...")
#     audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
#     sd.wait()
#     return audio_data
# 
# 
# def save_audio_to_wav(audio_data, file_path):
#     with wave.open(file_path, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)
#         wf.setframerate(sample_rate)
#         wf.writeframes(audio_data.tobytes())
# 
# 
# def transcribe_audio(file_path):
#     transcriber = aai.Transcriber()
#     transcript = transcriber.transcribe(file_path)
# 
#     # Print the transcription to the console
#     print(transcript.text)
# 
#     # Store all spoken words in the all_words_phrases collection
#     all_words_phrases_collection.insert_one({"text": transcript.text})
# 
#     # Check if the transcribed text matches any phrases in the dictionary
#     matching_phrases = [phrase for phrase in local_phrases_dict if phrase in transcript.text]
# 
#     if matching_phrases:
#         print("Matches found:")
#         for match in matching_phrases:
#             print(f"- {match}")
# 
#         try:
#             subprocess.run(["python", "transmit.py"], check=True)
#             print("transmit.py executed.")
#         except subprocess.CalledProcessError as e:
#             print(f"Error running transmit.py: {e}")
#     else:
#         print("No matches found.")
# 
# 
# if __name__ == "__main__":
#     # Record audio from the microphone
#     audio_data = record_audio()
# 
#     # Save the recorded audio to a temporary WAV file
#     temp_wav_file = "temp_audio.wav"
#     save_audio_to_wav(audio_data, temp_wav_file)
# 
#     # Transcribe the saved audio file
#     transcribe_audio(temp_wav_file)
# 
#     # Clean up: delete the temporary audio file
#     os.remove(temp_wav_file)

import assemblyai as aai
import subprocess
import sounddevice as sd
import numpy as np
import os
import wave
import json
from pymongo import MongoClient
from datetime import datetime  # Import datetime module for timestamping

# Replace with your AssemblyAI API key
aai.settings.api_key = "523057ab8c494c6ba1d31121c46dc99a"

# MongoDB configuration
mongo_client = MongoClient('mongodb+srv://kclarke:Tuesday19%40%40%40%40@cluster0.rhizd3g.mongodb.net/')  # Update with your MongoDB connection string
db = mongo_client.ENC_Word_Sets
all_words_phrases_collection = db.all_words_phrases
matched_neg_words_collection = db.matched_neg_words  # Collection for matched negative words

# Set the microphone parameters
sample_rate = 44100  # Adjust based on your microphone's sample rate
duration = 10  # Set the duration for audio capture in seconds

# Load local phrases from the attached JSON content and create a dictionary
json_content = {
    "phrases": [
"Encounter home",
    "Encounter Go Go.",
    "Step out of the car.",
    "This is ridiculous.",
    "I know my rights.",
    "You can't do this.",
    "I didn't do anything wrong.",
    "I wasn't speeding.",
    "This is unfair.",
    "Why did you pull me over?.",
    "You have no right to stop me.",
    "I don't have to show you my ID.",
    "I won't step out of the vehicle.",
    "You're just targeting me.",
    "This is discrimination.",
    "I want to speak to your supervisor.",
    "Get someone higher up here.",
    "This is ridiculous!.",
    "I can't believe this is happening.",
    "I know my rights!.",
    "You can't do this to me.",
    "What's going to happen now?.",
    "I need to get to.",
    "I know the law better than you do.",
    "I'm running late.",
    "I didn't see the speed limit sign.",
    "I had an emergency.",
    "Why are you hassling me?.",
    "You're just out to get people.",
    "This is an abuse of power.",
    "You're making things up.",
    "I don't have to answer your questions.",
    "I'm not doing anything you say.",
    "I don't trust cops.",
    "You're just trying to trick me.",
    "This is ridiculous.",
    "I can't believe I'm being pulled over.",
    "Just give me the ticket and let me go.",
    "Hurry up and finish this.",
    "I shouldn't be dealing with this.",
    "This is a waste of my time.",
    "Victim Mentality:.",
    "Why is everyone always picking on me?.",
    "I never catch a break.",
    "I'm not a criminal.",
    "I'm not a threat.",
    "Other people were driving faster than me.",
    "You're all just trying to meet a quota.",
    "This is a setup.",
    "Can we get this over with?.",
    "I have places to be.",
    "Why are you bothering me?.",
    "Don't you have anything better to do?.",
    "Explain why you pulled me over.",
    "Tell me exactly what I did wrong.",
    "This is an outrage!.",
    "You're ruining my day.",
    "I don't believe I was speeding.",
    "Are you sure about this?.",
    "Cops are just power-hungry.",
    "I've never been pulled over before.",
    "I can't believe this is happening to me.",
    "Can't you let me off with a warning?.",
    "I promise it won't happen again.",
    "Just my luck.",
    "This is a joke.",
    "I don't have time for this.",
    "Why do these things always happen to me?.",
    "I'm having the worst day."
      
    ]
}

local_phrases_dict = {phrase: True for phrase in json_content["phrases"]}

def record_audio():
    print("Recording audio. Speak now...")
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    return audio_data

def save_audio_to_wav(audio_data, file_path):
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)

    # Print the transcription to the console
    print(transcript.text)

    # Store all spoken words in the all_words_phrases collection
    all_words_phrases_collection.insert_one({"text": transcript.text})

    # Check if the transcribed text matches any phrases in the dictionary
    matching_phrases = [phrase for phrase in local_phrases_dict if phrase in transcript.text]

    if matching_phrases:
        print("Matches found:")
        for match in matching_phrases:
            print(f"- {match}")

            # Write matched phrases to the matched_neg_words collection with a timestamp
            matched_neg_words_collection.insert_one({"text": match, "timestamp": datetime.now()})
        
        try:
            subprocess.run(["python", "transmit.py"], check=True)
            print("transmit.py executed.")
        except subprocess.CalledProcessError as e:
            print(f"Error running transmit.py: {e}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    # Record audio from the microphone
    audio_data = record_audio()

    # Save the recorded audio to a temporary WAV file
    temp_wav_file = "temp_audio.wav"
    save_audio_to_wav(audio_data, temp_wav_file)

    # Transcribe the saved audio file
    transcribe_audio(temp_wav_file)

    # Clean up: delete the temporary audio file
    os.remove(temp_wav_file)
subprocess.run(["python", "chart_data.py"])



#  