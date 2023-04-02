import os
from pathlib import Path
DEFAULT_PATH = "HarbingerVault"

def load_path():
    if(not os.path.isdir(DEFAULT_PATH) or not os.path.exists(DEFAULT_PATH)):
        return
    
    messages = [
        {
            "role": "system", "content": "This is HarbingerCLI. An OpenAI API CLI program that intends to interface with ChatGPT within the software's own documentation."
            },
        {
            "role": "system", "content": "The following system messages will be a series of markdown filenames and their file contents. I would like you to note this and their contents."
            }
        ]
    
    for file in os.listdir(DEFAULT_PATH):
     filename = os.fsdecode(file)
     relative_path = os.path.join(DEFAULT_PATH, filename)
     if filename.endswith(".md"): 
         # print(os.path.join(directory, filename)) 
        with open(relative_path, 'r') as file:
            data = file.read().replace('\n', '')
            message = create_message(data, filename, relative_path)
            messages.append(message[0])
            messages.append(message[1])
        continue
     else:
         continue
     
    messages.append({
            "role": "system", "content": "There are no more markdown files. Can you please echo how many files have been processed?"
            })
     
    return messages

def create_message(file_content, file_name, relative_path):
    return [
        {
            "role": "system", "content": "This next markdown file is titled {}. Its relative path is {}. Its contents will be in the next system message.".format(file_name, relative_path)
        },
        {
            "role": "system", "content": file_content
        }
        ]
        
if __name__ == "__main__":
    load_path()