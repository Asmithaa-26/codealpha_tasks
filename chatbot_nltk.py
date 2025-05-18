import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi :)"]],
    [r"how are you?", ["I'm doing great, thanks!", "All good! How about you?"]],
    [r"(i'm|i am|i feel) (.*)", ["Why do you feel %2?", "What made you feel %2?"]],
    [r"(.*) your name?", ["I'm ChatBot, your virtual buddy!"]],
    [r"what is your name?", ["You can call me ChatBot 😄"]],
    [r"what can you do?", ["I can chat with you and make your day better! 😎"]],
    [r"(.*) (created|made) you?", ["I was created by a curious mind like yours!"]],
    [r"what (.*) like to do?", ["I love chatting and helping people!"]],
    [r"(.*) (weather|climate) (.*)", ["I'm not sure, but I hope it's nice where you are ☀️"]],
    [r"do you have hobbies?", ["Yes! Chatting with you is my favorite thing to do!"]],
    [r"tell me a joke", ["Why don’t programmers like nature? It has too many bugs! 😂"]],
    [r"i'm bored", ["How about reading a book or going for a walk?"]],
    [r"what is (.*)\?", ["Why do you ask about %1?"]],
    [r"(.*) (study|student|college)", ["Studying is great! What subject are you interested in?"]],
    [r"(.*) favorite (.*)", ["I like everything that makes people smile 😊"]],
    [r"(.*) (sad|upset|depressed)", ["I'm here for you ❤️ Want to talk about it?"]],
    [r"(.*) love (.*)", ["Love is a beautiful thing 💖"]],
    [r"(.*) happy (.*)", ["Happiness is best when shared!"]],
    [r"bye|exit|quit", ["Goodbye! 👋", "See you later!", "Take care!"]],
    [r"(.*)", ["Hmm... I didn't quite get that. Try asking differently? 🤔"]]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("🤖 ChatBot: Hello! Type 'bye' to end the chat.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
