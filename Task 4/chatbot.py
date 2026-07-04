def get_response(user_input):
    message = user_input.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    run_chatbot()
