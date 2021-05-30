from flask import Flask, request
from flask_cors import CORS
from chatterbot import ChatBot

chatbot = ChatBot('Bot')

app = Flask(__name__)
CORS(app)

@app.route('/api/chatbot', methods=['POST'])
def process():
	text = request.json['text']
	response = str(chatbot.get_response(text))
	output = {'output':response}
	return output
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)