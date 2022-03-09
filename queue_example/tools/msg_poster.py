from random import choice
import requests
from datetime import datetime


URL = "http://127.0.0.1:5000/messages"
GREETINGS = [
    "Hello",
    "Howdy",
    "How are you?",
    "Greeting",
    "Boas",
    "Hola",
    "Hey",
]

def post_greeting():
    greeting = {"messages": ""}
    greeting["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
    greeting["messages"] = choice(GREETINGS)
    response = requests.post(URL, json= greeting)
    if response.status_code== 204:
        print("Messages posted.")

    else:
        print("Error recieved.")


if __name__ == "__main__":
    for _ in range(100):
        post_greeting()
