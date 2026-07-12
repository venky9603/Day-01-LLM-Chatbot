from app.llm import generate_response


def main():

    print("=" * 50)
    print("Gemini LLM Chatbot")
    print("Type 'exit' to stop")
    print("=" * 50)


    while True:

        user_input = input("\nYou: ")


        if user_input.lower() == "exit":
            print("Goodbye!")
            break


        if not user_input.strip():
            print("Please enter a valid prompt.")
            continue


        response = generate_response(user_input)

        print("\nAssistant:", response)



if __name__ == "__main__":
    main()