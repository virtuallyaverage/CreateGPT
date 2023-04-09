from colorama import init, Fore, Style
import json
from os import getcwd
from os.path import join

module_folder = join(getcwd(), 'modules', "story_writer")

# Initialize colorama on Windows
init()  
print(Fore.GREEN+f"\n{'*'*109}\n\n\t\t\tWriting Prompt generator\n\n")
print(f"{'*'*109}\n")#+ Style.RESET_ALL)

program_options = ["Create new Outline", "Use Predefined Outline", "Create a Randomized Story (not recommended)"]
print(Fore.CYAN+f"Options:")
for index, option_name in enumerate(program_options):
    print(f"{index+1}) {program_options[index]}")

should_quit = False
while should_quit == False:
    try:
        user_selection = int(input(f"Task: (1-{len(program_options)}) "))-1
    except ValueError:
        print("Invalid selection, please try again\n")
        continue
        
        
    if user_selection < len(program_options) and user_selection >= 0:
        print(f"starting operation: {program_options[user_selection]}")
        should_quit = True
        #package into tuple of the name and index of the value
        program_selected = program_options[user_selection]
        continue
        
    else:
        print("Invalid selection, please try again\n")

from work_outline import WorkOutline
instance = WorkOutline()
if program_selected == "Create new Outline":
    outline = instance.newOutline()
    should_save = input(Fore.GREEN+"Save the created outline? The Outline CANNOT be saved at another time (y/n) ")
    if should_save == "y":
        outline_name = input("Outline Name: ")
        instance.SaveOutline(outline, outline_name)
        
    else:
        #give the option again
        be_sure = input("Are you sure you don't want to save? (y/n)")
        if be_sure == "y":
            outline_name = input("Outline Name: ")
            instance.SaveOutline(outline, outline_name)
    
    
#if we need to load in an outline
elif program_selected == "Use Predefined Outline":
    #print available options
    outline_options = instance.GetAvailableOutlines()
    print(Fore.CYAN+"Outlines:")
    for index, outline_file in enumerate(outline_options):
        print(f"{index+1}) {outline_file[:-5]}")
        
    #get users input
    chosen_index = int(input(f"Which outline you would like to use? (1-{len(outline_options)} )"))-1
    file_name =  outline_options[chosen_index]
    outline = instance.LoadOutline(file_name)
    print(f"Loaded outline named: {file_name[:-5]}\n")
    
#if we need to load the random thing
elif program_selected == "Create a Randomized Story (not recommended)":
    outline = instance.LoadOutline("random.json")
    print("")
    
    
############start generating prompts
from prompt_builder import PromptBuilder
prompt_builder = PromptBuilder(outline)
with open(join(module_folder, 'steps.json'), "r") as file:
    step_sequence = json.load(file)

step_to_perform = ''
while True:
    print(Fore.CYAN+"Which step to do?:")
    step_name_index = []
    index = 1
    for step_name, step in step_sequence.items():
        print(f"{index}) {step_name}; {step['print name']}")
        index += 1
        step_name_index.append(step_name)
        
    step_to_perform_index= input(f"which step do you want to work on? (1-{len(step_name_index)}, done) ")
    if step_to_perform_index != 'done':
        step_to_perform_name = step_name_index[int(step_to_perform_index)-1]
        step_to_perform = step_sequence[step_to_perform_name]
    else:
        break
    
    #see which result we go to
    if step_to_perform_name == 'fill in':
        prompt = prompt_builder.FillInStep(outline, step_to_perform)
        
    elif step_to_perform_name == 'get outline':
        data = input("What terms do you want to base the prompt off of?")
        num_to_split = input("how many elements should the story be split into? (3-7) ")
        
        prompt = prompt_builder.getOutline(data, num_to_split, step_to_perform)
        
    
    elif step_to_perform_name == 'write piece':
        print("writing apiec of work")
        pass
    elif step_to_perform_name == 'reflect piece':
        print("reflecting on the piece of work")
        pass
    elif step_to_perform_name == 'combine parts':
        print("combine two parts")
        pass
    elif step_to_perform_name == '':
        print("nothing")
        pass
    
    print(Fore.GREEN+f"Prompt for {step_to_perform_name}:\n\n")
    print(prompt+"\n\n")

print("Finished the story writer program")