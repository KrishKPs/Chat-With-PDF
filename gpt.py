from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from the .env file
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
openai.api_key = api_key

name = input("Enter the name for the resume file: ")   

file_path = "/Users/krishpatel/Desktop/Extracted text/"
file_name = f"{name}_text.txt"     
total_path = os.path.join(file_path, file_name)     

with open(total_path, "r") as file: 
    content = file.read() 

# Use OpenAI API to process the content
messages = [
    {"role": "system", "content": "You are a helpful assistant."},  
    {"role": "user", "content": content}
]

print("Processing content with OpenAI API...")   

while True:
    user_input = input("Ask your Question: ")

    if user_input.lower() == "exit":
        print("Exiting...")  
        break

    messages.append({"role": "user", "content": user_input}) 

    # Updated API Call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Updated Response Handling
    Ai_response = response['choices'][0]['message']['content']
    print(f"AI: {Ai_response}")  

    messages.append({"role": "assistant", "content": Ai_response})
