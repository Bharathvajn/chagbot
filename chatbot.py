def simple_chatbot():
    print("Welcome! I'm a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that.")

# Start the chatbot
simple_chatbot()
