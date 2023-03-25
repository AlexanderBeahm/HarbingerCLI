import click
    
@click.command()
@click.option("--help", help="Sovereign CLI -- Under Construction")    
def main():
    """Main entrypoint for CLI.
    """
    #TODO Create the loop back into Chat-GPT so that we can eventually train it to be a personal assistant.
    #For now this will serve as a root menu to access various chatgpt functions. Likely this will be removed for new 

if __name__ == '__main__':
    main()