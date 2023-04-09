# CreateGPT
CreateGPT is a modular command-line framework designed to generate structured prompts. It can be used to create long-form cohesive writing and larger coding projects. Although it currently has limited functionality, many more modules and features are planned for future updates.

# About
CreateGPT aims to automate a large part of the data formatting and structuring process for prompts, making it more efficient. While a decent amount of knowledge is still required to get ChatGPT to produce desired outputs, this tool has shown impressive results in reducing token count used by programmatically created data and improving GPT-4 performance.

# Installation
*Ensure you have a default Python 3 installation. Any modern version should be fine.
* install the ```colorama``` module by running ```pip install colorama```
* Copy or clone the repository to any folder

# Running
* Open a command prompt or PowerShell window and navigate to the base folder containing create_prompt.py: ```cd path/to/folder/with/create_prompt.py```
* Run ```python create_prompt.py```
* To directly access a module without having to select it, run: ```python modules/module_name/module_name.py```

# Current Functionality
___Story Writer___
Prompting methods | Completeness
-------------       |----------------
Fill Uspecified          |Finished
Get Outline          |Finished
Write Section          |Finished
fix/reflect section          |50%
Combine sections       |20%
