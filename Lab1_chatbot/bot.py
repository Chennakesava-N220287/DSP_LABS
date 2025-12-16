# bot.py
import nltk
nltk.download('punkt_tab')
# bot.py
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")"""
    
    
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)

# Train using WhatsApp chat
corpus = clean_corpus("chat.txt")
trainer.train(corpus)

print("🤖 Chatbot trained! Type 'exit' to quit.\n")

while True:
    query = input("> ")
    if query.lower() in ("exit", "quit", ":q"):
        break
    print("🪴", chatbot.get_response(query))