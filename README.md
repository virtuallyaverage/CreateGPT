# CreateGPT
This is a modular command-line tool to generate structured prompts, which can be used to create things like long-form cohesive writing and larger coding projects
Note: Though there is very limited functionality at the moment, many more modules and features are planned for the future

# About
This tool is meant to automate a large part of the data formatting and structuring of prompting out of the way in an effecient manner. A decent amount of knowlege is still needed to get ChatGPT to give you what you want. That said though, I have seen impressive results with lowering both the token count used by programmatically created data, as well as keeping GPT3.5 on the rails and squeezing absolutely impressive results from GPT4.

# Installation
* The only requirement other than a default ```python 3``` install (any modern version should be fine) for this project is the ```colorama``` module and can be installed by a simple ```pip install colorama```
* Copy or clone the repository to any folder

# Running
* Open a command prompt or powershell window to the base folder ```cd path/to/folder/with``` create_prompt.py in it
* then run ```python create_prompt.py```
* you can run ```python modules/module_name/module_name.py``` to directly access a module without having to select it.

# What Currently Works
module name     | Prompting methods | Completeness
------------- | -------------       |----------------
element  | Fill Uspecified          |Finished
element  | Get Outline          |85%
element  | Write Section          |60%
element  | fix/reflect section          |50%
element  | Combine sections       |20%
