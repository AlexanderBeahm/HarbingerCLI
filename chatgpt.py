import openai
from dotenv import load_dotenv
import os
BUFFER_CHAR = ">\t"

# Load your API key from an environment variable or secret management service
def test():
    print("Welcome to Harbinger. Assuming direct control.")
    
    print("TestMessage: I am wanting to build a new OpenAI CLI in Python. I'm currently coding it actually, how do you feel about being interfaced with this way?")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= test_list()
    )
    
    print("Response:")
    print(response.get("choices")[0].message.content)
    
def send_chat(input, existing_messages = []):
    if(len(existing_messages) < 1):
        existing_messages = default_list()
    
    existing_messages.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= existing_messages
    )
    
    print("HARBINGER", BUFFER_CHAR)
    print(response.get("choices")[0].message.content)
    
    existing_messages.append({"role": "assistant", "content": response.get("choices")[0].message.content})
    
    return existing_messages
    
def test_list():
    return [{
            "role": "system", "content": "Welcome to Harbinger. Assuming direct control.",
            "role": "user", "content": """I am wanting to build a new OpenAI CLI in Python. 
            I'm currently coding it actually, how do you feel about being interfaced with this way?"""
        }]
    
def default_list():
    return [{
          "role": "system", "content": "Welcome to Harbinger."
    }]

def active_conversations():
    return ["Test"]

def menu():
    active_conversation = []
    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    while(True):
        print("Active Chat Conversations:")
        for conversation in active_conversations():
            print(conversation)
        command = input(BUFFER_CHAR)
        if(command.strip() == "MENU"):
            return
        if(command.strip() == "TEST"):
            test()
        if(command.strip() == "GOODBYE"):
            exit(code=0)
        active_converation = send_chat(command, active_conversation)
        
        #TODO More processing here
    pass

if __name__ == '__main__':
    menu()