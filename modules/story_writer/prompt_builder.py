class PromptBuilder():
    def __init__(self, outline) -> None:
        self.outline = outline
    
    def FillInStep(self, outline_data:dict, step_info:dict) -> str:
        prompt:str  = step_info['base prompt']
        prompt_parts:list = prompt.split('#')
        
        #trim the data
        trimmed_data = self.trimData(outline_data)
        
        # Replace the keys with named placeholders
        prompt = prompt.replace("#D", "{data}")

        # Insert the variables into their respective placeholders
        formatted_prompt = prompt.format(data=trimmed_data)
        
        return formatted_prompt
    
    
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
                    print("no subfields")
                
                else:
                    #itterate through the subfields
                    for subfield_name in working_element['sub_fields']:
                        subfield = working_element['sub_fields'][subfield_name]
                        subfield.pop('units')
                        subfield.pop('prompt')
        return outline_data