from colorama import init, Fore, Style
import json

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
        print(f"starting operation: {program_options[user_selection]}\n")
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
    should_save = input(Fore.CYAN+"Save the created outline? The Outline CANNOT be saved at another time (y/n) ")
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
    print(f"Loaded outline named: {file_name[:-5]}")
    


print("Finished the story writer program")