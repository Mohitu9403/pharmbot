# Imports 

from typing import List 
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#chatbot = ChatBot('Training Example')
#trainer = ListTrainer(chatbot)



application = Flask(__name__, template_folder="template")
app = application
#create chatbot
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

#define app routes
@application.route("/")
def index():
    return render_template("index.html")

@application.route("/get")


#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    application.run()