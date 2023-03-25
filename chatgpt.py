import openai

# Load your API key from an environment variable or secret management service
def test():
    print("Welcome to Harbinger. Assuming direct control.")
    
    print("TestMessage: I am wanting to build a new OpenAI CLI in Python. I'm currently coding it actually, how do you feel about being interfaced with this way?")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system", "content": "Welcome to Harbinger. Assuming direct control.",
            "role": "user", "content": """I am wanting to build a new OpenAI CLI in Python. 
            I'm currently coding it actually, how do you feel about being interfaced with this way?"""
        }]
    )
    
    print("Response:")
    print(response.get("choices")[0].message.content)

if __name__ == '__main__':
    test()