from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Bot')
trainer = ListTrainer(chatbot)

trainer.train() #Put a conversation here in list of string to train from.