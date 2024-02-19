import requests
import subprocess

def send_sms(api_key, phone_number, message):
    api_url = "https://textbelt.com/text"
    
    payload = {
        'phone': phone_number,
        'message': message,
        'key': api_key,
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            print("SMS sent successfully!")
        else:
            print(f"Failed to send SMS. Response code: {response.status_code}, Response text: {response.text}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Replace with your Textbelt API key, recipient phone number, and message
textbelt_api_key = "5a590ad7d2bc5b8c6642663cef5ac56f5127c936C4C8N17UZe5xRD4lsQMRPjxAx"
recipient_phone_number = "+14704045798"  # Include the country code
message = "Please go to your Encouter Engineering Dashboard immedialy:http://192.168.1.119:8501"


# Call the function to send SMS
send_sms(textbelt_api_key, recipient_phone_number, message)
subprocess.run(["python", "flask_server.py"])
subprocess.run(["python", "chart_data.py"])