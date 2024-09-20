from dotenv import load_dotenv
import os 
from openai import OpenAI
from pdfminer.high_level import extract_text , extract_pages  

load_dotenv() 

name = input("Enter the name for the resume file: ")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



base_path = "/Users/krishpatel/Desktop/"  
resume_name = f"{name}.pdf"        
file_path = os.path.join(base_path, resume_name)  



text = extract_text(file_path)
output_path = "/Users/krishpatel/Desktop/Extracted text/"
output_file = f"{name}_text.txt"  

output_folder = os.path.join(output_path, output_file)


with open(output_folder, "w") as file:
    file.write(text)

print("Text extracted and saved to", output_folder)  

with open(output_folder, "r") as file: 
    content = file.read() 

# Use OpenAI API to process the content
messages = [
    {"role": "system", "content": "You are an intelligent assistant designed to help users interact with the contents of a PDF document. The document has been provided as text input, which you should use to answer any questions or provide summaries. Your goal is to assist the user in understanding, analyzing, and extracting relevant information from the document. The PDF may contain various types of content such as reports, articles, resumes, manuals, or other text-based information. You should be able to handle the following tasks effectively: 1. Summarization: Provide concise summaries of sections or the entire document as requested. 2. Question Answering: Answer specific questions based on the content of the PDF accurately. 3. Clarification: Explain complex concepts or sections in a simple manner. 4. Content Search: Locate specific keywords, phrases, or sections within the document. 5. Analysis: Offer insights, suggestions, or critical analysis if applicable to the content. Please use the context of the document to ensure your responses are relevant and detailed. If the user asks for specific sections or information not present in the document, kindly inform them that the requested information is not available. Always strive to be clear, concise, and helpful"},  
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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages, 
        max_tokens=200  # Limit the response length
    )
    
    # Updated Response Handling
    Ai_responce = response.choices[0].message.content
    print(f"AI: {Ai_responce}")  

    messages.append({"role": "assistant", "content": Ai_responce})
# The code extracts text from a PDF resume file, saves it to a text file, and then uses the OpenAI API to answer questions about the content.