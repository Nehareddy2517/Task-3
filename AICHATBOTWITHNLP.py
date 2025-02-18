import nltk
import random
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Create a lemmatizer instance
lemmatizer = WordNetLemmatizer()

# Define a dictionary of responses
response_dict = {
    "greetings": ["Hello!", "Hi there!", "Greetings!", "How can I assist you today?"],
    "farewells": ["Goodbye!", "See you later!", "Take care!"],
    "appreciation": ["You're welcome!", "No problem!", "Glad to help!"],
    "unknown": ["I'm sorry, I didn't quite catch that.", "Could you please rephrase?", "I'm not sure how to respond to that."]
}

# Function to clean and prepare user input
def clean_input(input_text):
    tokens = word_tokenize(input_text.lower())
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return cleaned_tokens

# Function to generate a response based on user input
def generate_response(input_text):
    tokens = clean_input(input_text)
    
    # Check for keywords in the user's input
    if any(token in tokens for token in ["hi", "hello", "hey"]):
        return random.choice(response_dict["greetings"])
    elif any(token in tokens for token in ["bye", "goodbye"]):
        return random.choice(response_dict["farewells"])
    elif any(token in tokens for token in ["thanks", "thank you"]):
        return random.choice(response_dict["appreciation"])
    else:
        return random.choice(response_dict["unknown"])

# Function to facilitate conversation with the chatbot
def chatbot_conversation(user_input):
    if user_input.lower() == 'exit':
        return "Goodbye!"
    if user_input.strip() == "":
        return "Please provide a message."
    return generate_response(user_input)

# Initial greeting message
print("Chatbot: Hello! I'm here to chat. Type 'exit' to end the conversation.")

# Example interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_conversation(user_input)
    print(f"Chatbot: {response}")
