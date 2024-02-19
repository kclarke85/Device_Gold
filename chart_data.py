from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb+srv://kclarke:Tuesday19%40%40%40%40@cluster0.rhizd3g.mongodb.net/")
db = client["ENC_Word_Sets"]

def extract_text_and_write_json(collection_name, file_name):
    collection = db[collection_name]
    result_list = []

    # Fetch documents from the collection
    for doc in collection.find():
        # Extract text fields only
        text_fields = {key: value for key, value in doc.items() if isinstance(value, str)}
        result_list.append(text_fields)

    # Write the text fields to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(result_list, json_file, indent=4)

    return result_list

# Call the function for the app_words_phrases collection
all_words_phrases_data = extract_text_and_write_json('all_words_phrases', 'all_words_phrases.json')

# Convert each item in all_words_phrases_data to a dictionary
all_words_phrases_data = [dict(item) for item in all_words_phrases_data]

# Call the function for the matched_neg_words collection
matched_neg_words_data = extract_text_and_write_json('matched_neg_words', 'matched_neg_words.json')

# Insert data into collections
all_words_phrases_collection = db["all_words_phrases"]
matched_neg_words_collection = db["matched_neg_words"]

# Delete existing data in collections
all_words_phrases_collection.delete_many({})
matched_neg_words_collection.delete_many({})

# Insert new data into collections
all_words_phrases_collection.insert_many(all_words_phrases_data)
matched_neg_words_collection.insert_many(matched_neg_words_data)
