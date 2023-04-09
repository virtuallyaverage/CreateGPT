class WorkOutline():
    def __init__(self) -> None:
        from json import load, dump
        from os import getcwd, makedirs
        from os.path import join, exists
        self.os_join = join
        self.os_exists = exists
        self.load = load
        self.dump = dump
        
        #get the outline folder
        self.working_directory = getcwd()
        self.outline_folder = join(self.working_directory, 'modules', 'story_writer', 'story_writer_outlines')
        does_path_exist = exists(self.outline_folder)
        if not does_path_exist:
            makedirs(self.outline_folder)
            print("Could not find the outline folder, so a new one was made")
        
        pass
    
    def newOutline(self) -> dict:
        
        #get the default template
        with open(self.os_join(self.outline_folder, 'default.json')) as file:
            user_outline = self.load(file)
            
        #start getting the info from the user
        user_outline = self.QuizUser(user_outline)
        
        #return it
        return user_outline

     
    def LoadOutline(self, file_name) -> dict:
        #get the default template
        print(file_name)
        with open(self.os_join(self.outline_folder, file_name)) as file:
            user_outline = self.load(file)
        
        #return it
        return user_outline
    
    def GetAvailableOutlines(self) -> list:
        from  os import walk
        for _, _, files in walk(self.outline_folder):
            #sort out potential files that aren't json
            outlines =  [file_name for file_name in files if file_name[-4:] == 'json']  
        return outlines
    
    def SaveOutline(self, outline, outline_name):
        file_path = self.os_join(self.outline_folder, f"{outline_name}.json")
        
        proven_path = False
        while not proven_path:
            does_path_exist = self.os_exists(file_path)
            if does_path_exist:
                overwrite = input("A file with that name already exists. Overwrite it? (y/n)").lower()
                if overwrite == 'y':
                    #just continue
                    print("Overwriting")
                    proven_path = True
                elif overwrite == "n":
                    #get the new name and redo the loop
                    outline_name = input("not overwriting, please select a new name: ")
                    file_path = self.os_join(self.outline_folder, file_path, f"{outline_name}.json")
                else:
                    print("error with your answer, please retry")
                    
            else:
                #if the file does not exist, just continue
                proven_path = True
                
        with open(file_path, "w") as file:
            self.dump(outline, file, indent=4)
        

    def QuizUser(self, outline:dict) -> dict:
        from colorama import init, Fore, Style
        # Initialize colorama on Windows
        init()  
        print(Fore.BLUE+f"\n{'*'*109}\n\n\tFill out each question to create your outline\n")
        print("\tNote: enter s, or skip to have the ai guess those values")
        print(f"\n\n{'*'*109}\n"+ Style.RESET_ALL)

        #words that will skip the input
        skip_alias = ["skip", "no", "pass", "n", "p", "s", ""]
        
        #itterate through the subdivision of topics
        for subdivision, _ in outline.items():
            
            print(Fore.MAGENTA+f"\n{'-'*30} Questions about the stories: {subdivision} elements {'-'*30}\n"+Style.RESET_ALL)   
            
            #itterate through the elements in a subdivision
            for element_name, _ in outline[subdivision].items():
                working_element = outline[subdivision][element_name]
                
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
        return outline
