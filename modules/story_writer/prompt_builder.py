class PromptBuilder():
    def __init__(self, outline) -> None:
        self.outline = outline
    
    def FillInStep(self, outline_data:dict, step_info:dict) -> str:
        prompt:str  = step_info['base prompt']
        
        #trim the data
        trimmed_data = self.trimData(outline_data)
        #condense to string
        trimmed_data = self.condense_dict(trimmed_data)
        
        # Replace the keys with named placeholders
        prompt = prompt.replace("#D", "{data}")

        # Insert the variables into their respective placeholders
        formatted_prompt = prompt.format(data=trimmed_data)
        
        return formatted_prompt
    
    def getOutline(self, outline_data:str, num_parts:str, step_info:dict) -> str:
        
        prompt:str  = step_info['base prompt']
        
        # Replace the keys with named placeholders
        prompt = prompt.replace("#D", "{data}")
        prompt = prompt.replace("#P", "{parts}")

        # Insert the variables into their respective placeholders
        formatted_prompt = prompt.format(data=outline_data, parts=num_parts)
        
        return formatted_prompt
    
    def writeASection(self, outline:str, data:str, step_info:dict):
        prompt:str  = step_info['base prompt']
        
        # Replace the keys with named placeholders
        prompt = prompt.replace("#D", "{data}")
        prompt = prompt.replace("#O", "{outline}")

        # Insert the variables into their respective placeholders
        formatted_prompt = prompt.format(data=data, parts=outline)
        return formatted_prompt
    
    def condense_dict(self, d:dict, separator='|'):
        condensed = []
        
        for k, v in d.items():
            key = k  # Use the first 3 characters of the key as an abbreviation
            
            if isinstance(v, dict):
                condensed_v = self.condense_dict(v, separator=separator)
                condensed.append(f"{key}({condensed_v})")
            else:
                value = 'N' if v is None else v  # Represent None values with 'N'
                condensed.append(f"{value}")
        
        return separator.join(condensed)

    def trimData(self, outline_data:dict):
        #itterate through the subdivision of topics
        for subdivision, _ in outline_data.items():
            #itterate through the elements in a subdivision
            for element_name, _ in outline_data[subdivision].items():
                working_element = outline_data[subdivision][element_name]
                working_element.pop('units')
                working_element.pop('prompt')
                
                #see if we have sub fields to work with
                if len(working_element['sub_fields']) <= 0:
                    working_element.pop('sub_fields')
                
                else:
                    #itterate through the subfields
                    for subfield_name in working_element['sub_fields']:
                        subfield = working_element['sub_fields'][subfield_name]
                        subfield.pop('units')
                        subfield.pop('prompt')
        return outline_data