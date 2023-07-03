import openai

openai.api_key = ''

def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the ChatGPT model
        prompt=message,
        max_tokens=50,  # Adjust the response length as needed
        n=1,  # Generate a single response
        stop=None,  # Stop generating responses at any token
        temperature=0.7,  # Control the randomness of the output
    )

    return response.choices[0].text.strip()

def main():
    print("Welcome! How can I assist you?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        
        response = send_message(user_input)
        
        print("ChatGPT: " + response)

# Run the main function
if __name__ == '__main__':
    main()
