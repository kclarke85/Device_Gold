#from flask import Flask, send_file
#app = Flask(__name__)
#$VIDEO_FILE_PATH = "/home/kclar/Encounter/output.mp4"

#@app.route("/video")
#def get_video():
    #return send_file(VIDEO_FILE_PATH, mimetype='video/mp4')

#if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify
import json

app = Flask(__name__)

GOOD_DATA_FILE_PATH = "/home/kclar/Encounter/all_words_phrases.json"
BAD_DATA_FILE_PATH = "/home/kclar/Encounter/matched_neg_words.json"

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

@app.route("/api/all_words_phrases", methods=['GET'])
def get_good_data():
    good_data = load_json_data(GOOD_DATA_FILE_PATH)
    return jsonify(good_data)

@app.route("/api/matched_neg_words", methods=['GET'])
def get_bad_data():
    bad_data = load_json_data(BAD_DATA_FILE_PATH)
    return jsonify(bad_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run on localhost with port 5000

