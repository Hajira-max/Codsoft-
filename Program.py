# Rule Based Chatbot
# A simple chatbot using if-else rules

print("Chatbot: Hi, I'm your assistant. Type 'bye' to quit.")

while True:
    user = input("You: ")

    # greetings
    if "Hi" in user or "Hello" in user:
        print("Chatbot: Hello there! How can I help you?")

    # asking how am I
    elif "How are you" in user:
        print("Chatbot: I'm fine (since I'm a bot 😅). What about you?")

    # if user says they are fine
    elif "I am fine" in user:
        print("Chatbot: Good to hear that!")

    # asking my name
    elif "Your name" in user:
        print("Chatbot: I'm just a simple chatbot written in Python.")

    # asking for help
    elif "Help" in user:
        print("Chatbot: Sure, tell me what you need help with.")

    # question 1 - Python
    elif "python" in user:
        print("Chatbot: Python is a high-level, general-purpose and user-friendly programming language.")

    # question 2 - Hard to use
    elif "hard" in user and "use" in user:
        print("Chatbot: Not at all. Even beginners can do projects using Python.")
     
    #Thank you condition 
    elif "Thank" in user:
        print("Your are welcome ")
    # goodbye
    elif "Bye" in user or "Exit" in user:
        print("Chatbot: Bye! Talk to you later 👋")
        break

    # default / unknown response
    else:
        print("Chatbot: Hmm... I don't understand that. Try something else.")# Task 1 - Rule Based Chatbot
while True:
    user = input("You: ")

    # greetings
    if "Hi" in user or "Hello" in user:
        print("Chatbot: Hello there! How can I help you?")

    # asking how am I
    elif "How are you" in user:
        print("Chatbot: I'm fine (since I'm a bot 😅). What about you?")

    # if user says they are fine
    elif "I am fine" in user:
        print("Chatbot: Good to hear that!")

    # asking my name
    elif "Your name" in user:
        print("Chatbot: I'm just a simple chatbot written in Python.")

    # asking for help
    elif "Help" in user:
        print("Chatbot: Sure, tell me what you need help with.")

    # question 1 - Python
    elif "python" in user:
        print("Chatbot: Python is a high-level, general-purpose and user-friendly programming language.")

    # question 2 - Hard to use
    elif "hard" in user and "use" in user:
        print("Chatbot: Not at all. Even beginners can do projects using Python.")
     
    #Thank you condition 
    elif "Thank" in user:
        print("Your are welcome ")
    # goodbye
    elif "Bye" in user or "Exit" in user:
        print("Chatbot: Bye! Talk to you later 👋")
        break

    # default / unknown response
    else:
        print("Chatbot: Hmm... I don't understand that. Try something else.")# Task 1 - Rule Based Chatbot
