from colorama import Fore, Style
import sys
import codecs, json


INSTRUCTIONS_FILE = "instructions.json"

def load_instructions():
    try:
        with open(INSTRUCTIONS_FILE, "r") as file:
            instructions = json.load(file)
        return instructions
    except FileNotFoundError:
        return {}

#def save_instructions(instructions):
#    with open(INSTRUCTIONS_FILE, "w") as outfile:
#        json.dump(instructions, outfile, indent=4)

def save_instructions(instructions):
    with codecs.open(INSTRUCTIONS_FILE, 'w', 'utf8') as f:
        f.write(json.dumps(instructions, sort_keys = True, ensure_ascii=False, indent=4))

def print_colored_dict(my_dict):
    for key, value in my_dict.items():
        for entry in value:
            desc = entry["desc"]
            info = entry["info"]
            path = entry["path"]
            if info[-1] == "=":
                print(f"  {Fore.GREEN}- {desc}:{Style.RESET_ALL}\n    {Fore.RED}{info}{Style.RESET_ALL}{path}\n")
            else:
                print(f"  {Fore.GREEN}- {desc}{Style.RESET_ALL}\n    {Fore.RED}{info}{Style.RESET_ALL} {path}\n")

def add_entry_to_dict(command, desc, info, path):
    instructions = load_instructions()
    
    if command not in instructions:
        instructions[command] = []
    
    new_entry = {
        'desc': desc,
        'info': info,
        'path': path
    }
    
    instructions[command].append(new_entry)
    save_instructions(instructions)
    print(f"Added a new entry for '{command}' to the dictionary.")
    print_colored_dict({command: instructions.get(command, [])})

if __name__ == "__main__":
    if len(sys.argv) == 2:
        command = sys.argv[1]
        instructions = load_instructions()
        print_colored_dict({command: instructions.get(command, [])})
    elif len(sys.argv) == 6 and sys.argv[1] == "--add":
        command = sys.argv[2]
        desc = sys.argv[3]
        info = sys.argv[4]
        path = sys.argv[5]
        add_entry_to_dict(command, desc, info, path)
    else:
        print("Usage: \n1. To view instructions: python wut.py <application name>\n2. To add a new entry: python wut.py --add <application name> <description> <info> <path>")
