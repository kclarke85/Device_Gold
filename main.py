import logging
import time
import speech_recognition as sr
from pymongo import MongoClient
from transmit import play_mp3, say_message
import subprocess
# Connect to MongoDB (replace with your MongoDB connection details)
try:
    client = MongoClient('mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc')
    db = client['webapp_subscribe']
    all_words_phrases_collection = db['all_words_phrases']
    spoken_negative_words_collection = db['spoken_negative_words']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Define negative keywords
negative_keywords = [
    "No", "Step out of the car", "This is ridiculous", "I know my rights", "You can't do this"
]

def detect_negative_words(text):
    for keyword in negative_keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def run_negative_functions():
    logging.info("Detected negative keywords.")
    path_to_mp3 = "/home/kclar/Encounter/transmit.mp3"
    message = "A potential negative encounter is underway. The device owner's family has been alerted."
    play_mp3(path_to_mp3)
    say_message(message)
    print("Negative keywords detected. Stopped the program.")

    # Add the following code to run camvid_out.py
    if __name__ == "__main__":
        try:
            subprocess.run(["python", "camvid_out.py"])
        except Exception as e:
            logging.error(f"Error running camvid_out.py: {e}")

def log_all_words_phrases(text):
    all_words_phrases_collection.insert_one({'text': text})
    print(f"Words and phrases logged to 'all_words_phrases' collection.")

def log_spoken_negative_words(text):
    spoken_negative_words_collection.insert_one({'text': text})
    print(f"Spoken negative words logged to 'spoken_negative_words' collection.")

def main():
    logging.basicConfig(filename='speech_recognition.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    recognizer = sr.Recognizer()

    while True:  # Run the program in an infinite loop
        with sr.Microphone() as source:
            print("Listening...")

            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=120)

                if audio:
                    print("Recognizing speech...")
                    text = recognizer.recognize_google(audio)
                    print("You said:", text)
                    log_all_words_phrases(text)

                    # Check for negative words and run functions if found
                    if detect_negative_words(text):
                        print("Negative words detected. Running functions.")
                        run_negative_functions()
                        log_spoken_negative_words(text)
                    else:
                        print("No negative words detected.")

                else:
                    print("No speech detected.")

            except sr.WaitTimeoutError:
                logging.error("Listening timed out. No speech detected.")
                print("Listening timed out. No speech detected.")
            except sr.UnknownValueError:
                logging.error("Speech Recognition could not understand audio")
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logging.error(f"Could not request results from Google Speech Recognition service; {e}")
                print(f"Could not request results from Google Speech Recognition service; {e}")

        # Add a delay before the next run (adjust as needed)
        time.sleep(30)  # Wait for 30 seconds before the next run

if __name__ == "__main__":
    main()
