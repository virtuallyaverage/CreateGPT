import json
from colorama import init, Fore, Style

#the name of the outline that was saved
element_filename = "outlines/first.json"

with open(element_filename, "r") as file:
    whole_database = json.load(file)
    
# Initialize colorama on Windows
init()  
print(Fore.BLUE+f"\n{'*'*109}\n\n\tCreate the outline prompt\n\n{'*'*109}\n"+ Style.RESET_ALL)

points_for_each_section = "Plot points: significant events that move the story or change the story direction. Plot points can include things like the inciting incident, the midpoint reversal, the climax, and the resolution. Character points: key moments or decisions in a story that reveal something important about a character's personality, motivations, or development. Theme points: recurring ideas or messages in a story that gives it deeper meaning or resonance."

#intitialise the prompt
prompt = f"Here are some specifics about a story I am writing. Considering ALL information given, write a detailed outline with 5 bullet points marking points in the stories progress. Do this by writing the bullet points, with a # before each. Then put all relevant information to write that section of the story, the goal is that you could write that section without any knowledge about what happened in the other sections.\n"# organize this information into categories: {points_for_each_section}\n"

# get a list of all of the elements
data_string = "Info:\n"
for category_name, _ in whole_database.items():
    data_string += f"{category_name}, ["
    for element_name, _ in whole_database[category_name].items():
        working_element = whole_database[category_name][element_name]
        if len(working_element['sub_fields']) <= 0:
            data_string += f"{element_name}: {working_element['input']}, "
        else:
            data_string += f"{element_name}: "
            for subfield_name in working_element['sub_fields']:
                subfield = working_element['sub_fields'][subfield_name]
                data_string += f"{subfield_name}> {subfield['input']}, "
                
    data_string += "]\n"

#add the data to the prompt
prompt += data_string

#have it deal with none fields
prompt += "Any data fields filled with \"None\" estimate an answer that fits the rest of the information and use that\n"

print(prompt)       