import json
from colorama import init, Fore, Style

#the name of the outline that was saved
element_filename = "outlines/s.json"

with open(element_filename, "r") as file:
    whole_database = json.load(file)
    
# Initialize colorama on Windows
init()  
print(Fore.BLUE+f"\n{'*'*109}\n\n\tCreate the outline prompt\n\n{'*'*109}\n"+ Style.RESET_ALL)

points_for_each_section = "Plot points: significant events that move the story or change the story direction. Plot points can include things like the inciting incident, the midpoint reversal, the climax, and the resolution. Character points: key moments or decisions in a story that reveal something important about a character's personality, motivations, or development. Theme points: recurring ideas or messages in a story that give it deeper meaning or resonance."

#intitialise the prompt
prompt = f"Here is some specifics about a story I am writing. Considering ALL information given, write a detailed outline with 5 bullet points. Do this by writing the bullet points, with a # before each, then expand on any topics covered in that section, organized into categories: {points_for_each_section}"

# get a list of all of the elements
data_string = "Info:\n"
for category in whole_database:
    data_string += f"{category}, ["
    for element in whole_database[category]:
        pass
    data_string += "]"
    
print(prompt)
        