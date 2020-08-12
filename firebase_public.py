from pyrebase import pyrebase

config = {  
"apiKey": "INSERT_API_KEY_HERE",  
"authDomain": "chat-bo-c5be1.firebaseapp.com",  
"databaseURL": "https://chat-bo-c5be1.firebaseio.com",  
"storageBucket": "chat-bo-c5be1.appspot.com",  
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

ChatBot = db.child("1ttg3LdOg7Vcq2ttzoiih7Ze4LIMKKZVrIkx_xkLFAM4").get()
ChatBotVal = ChatBot.val()
chatbot_items = ChatBotVal['ChatBot']
chatbot_words = ChatBotVal['Words']
chatbot_keys = ChatBotVal['Keys']

responsesDict = {}

for i in range(len(chatbot_items)):
    curr_item = chatbot_items[i]
    responsesDict[curr_item['key']] = curr_item['response']

wordArr = []
for i in range(len(chatbot_words)):
    wordArr.append(chatbot_words[i]['word'])

keyArr = []
for i in range(len(chatbot_keys)):
    keyArr.append(chatbot_keys[i]['key'])


