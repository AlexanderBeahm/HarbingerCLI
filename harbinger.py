import click
from dotenv import load_dotenv
import os
import openai
from chatgpt import menu, send_chat

BUFFER_CHAR = ">\t"

@click.group(invoke_without_command=True)
#//@click.pass_context # If we need to enable context from invoker, useful for command line args to quickly load configurations and states.
def cli():
    """Main entrypoint for CLI.
    """
    #TODO Create the loop back into Chat-GPT so that we can eventually train it to be a personal assistant.
    #For now this will serve as a root menu to access various chatgpt functions. Likely this will be removed for new 
    # if(len(args) > 0):
    #     pass
    
    try:
        load_dotenv()
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        while(True):
            command = input(BUFFER_CHAR)
            if(command.strip() == "CHAT"):
                menu()
            if(command.strip() == "GOODBYE"):
                exit(code=0)
            #TODO More processing here
        pass
    except:
        print("Server error occurred, shutting down.")
        
@click.command("chat")
def chat():
    menu()
    
if __name__ == '__main__':
    cli()