from colorama import init, Fore, Style
import json
import os
import subprocess


working_directory = os.getcwd()
modules_path = os.path.join(working_directory, 'modules')
assert os.path.exists(modules_path), f"'{modules_path}' folder does not exist."

try:
    with open("modules.json", "r") as file:
        installed_modules = json.load(file)
except json.decoder.JSONDecodeError as err:
    print("Error loading 'modlues.json' file. Make sure the file is not empty")
    exit()
except FileNotFoundError as err:
    print("'modules.json' not found in the base directory. Please make sure it exists and is not empty")
    exit()

    
# Initialize colorama on Windows
init()  
print(Fore.BLUE+f"\n{'*'*109}\n\n\t\t\tSelect your desired prompt generator:\n")


print("Installed Modules:\n")
module_name_index = 1
module_names = ['blank from module_names, shouldn\'nt be seen']
for module_name, _ in installed_modules.items():
    module_names.append(module_name)
    print(f"{module_name_index}) {module_name}, {installed_modules[module_name]['short description']}")
    module_name_index +=1

print(f"\n{'*'*109}\n")

should_quit = False
while should_quit == False:
    user_selection = int(input(Fore.GREEN+f"Generator you would like to use: (1-{len(module_names)-1})"))
    if user_selection < len(module_names) and user_selection >0:
        print(f"starting program: {module_names[user_selection]}\n")
        should_quit = True
        program_selected = installed_modules[module_names[user_selection]]
        #TODO: "implement starting the program"
        
    else:
        print("Invalid selection, please try again\n")
        
subprocess.run(["python", os.path.join("modules", program_selected['file name'])])
    