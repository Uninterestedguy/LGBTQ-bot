import random


bot_template = "Unite_Bot : {0}"
user_template = "User : {0}"

send_message(input("Let's chat"))

def respond(message):
    for key in intents.keys():
        if message in key:
            random.choice(intents[key])
    return response

def send_message(message):
    print(user_template.format(message))
    response = respond(message) 
    print(bot_template.format(response))
