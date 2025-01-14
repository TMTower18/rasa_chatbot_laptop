from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def index():
    php_response = requests.get('http://localhost:8000/index.php')
    return php_response.text

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']

    print("User Message:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I didn\'t understand that.'

    return jsonify({'response': bot_response})





if __name__ == "__main__":
    app.run(port=5000)


