import json
from colorama import init, Fore, Style

with open("user_defined_elements.json", "r") as file:
    elements = json.load(file)
  
# Initialize colorama on Windows
init()  
print(Fore.BLUE+f"\n{'*'*109}\n\n\tFill out each question to create your outline\n\n{'*'*109}\n"+ Style.RESET_ALL)

#words that will skip the input
skip_alias = ["skip", "no", "pass", "n", "p", "s"]
 
#itterate through the subdivision of topics
for subdivision, _ in elements.items():
    
    print(Fore.MAGENTA+f"\n{'-'*30} Questions about the stories: {subdivision} elements {'-'*30}\n"+Style.RESET_ALL)   
    
    #itterate through the elements in a subdivision
    for element_name, _ in elements[subdivision].items():
        working_element = elements[subdivision][element_name]
        
        #see if we have sub fields to work with
        if len(working_element['sub_fields']) <= 0:
            #get the user input
            user_input = input(Fore.CYAN+f"{working_element['prompt']} "+Style.RESET_ALL)
            
            #if the user wants to skip
            if user_input.lower() in skip_alias:
                print(Fore.CYAN+"A guess will be made that fits with the rest of the information provided\n"+Style.RESET_ALL)
                user_input = None
            else:
                print("")
                
            #push the user input to the file
            working_element["input"] = user_input
        else:
            #itterate through the subfields
            for subfield_name in working_element['sub_fields']:
                subfield = working_element['sub_fields'][subfield_name]
                user_input = input(Fore.CYAN+subfield['prompt']+" "+Style.RESET_ALL)
                
                #if the user wants to skip
                if user_input.lower() in skip_alias:
                    print(Fore.CYAN+"A guess will be made that fits with the rest of the information provided\n"+Style.RESET_ALL)
                    user_input = None
                else:
                    print("")
                    
                #push the user input to the file
                subfield["input"] = user_input
        
    
    
    
print(f"\n{'*'*60}\n\n\tYour inputs\n\n{'*'*60}\n")

#itterate through the subdivision of topics
for subdivision, _ in elements.items():
    
    print(Fore.MAGENTA+f"\n{'-'*30} Questions about the stories: {subdivision} elements {'-'*30}\n"+Style.RESET_ALL)   
    
    #itterate through the elements in a subdivision
    for element_name, _ in elements[subdivision].items():
        working_element = elements[subdivision][element_name]
        
        #see if we have sub fields to work with
        if len(working_element['sub_fields']) <= 0:
            #print the user input
            print(Fore.CYAN+f"{element_name}: "+f"{elements[subdivision][element_name]['input']}"+Style.RESET_ALL)   
        else:
            #itterate through the subfields
            for subfield_name in working_element['sub_fields']:
                subfield = working_element['sub_fields'][subfield_name]
                print(Fore.CYAN+f"{subfield_name}: "+f"{subfield['input']}"+Style.RESET_ALL)
                
                
file_name = input("file name? (no file extension e.g. .json)")        
    
   
    
with open(f"{file_name}.json", "w") as file:
    json.dump(elements, file, indent=4)
    
print(Fore.GREEN+"Outline created!"+Style.RESET_ALL)