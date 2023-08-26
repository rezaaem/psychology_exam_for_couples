import os

# Get the current directory where the Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get a list of all files in the current directory
file_list = os.listdir(current_dir)

# Iterate over each file in the directory
for file_name in filter(lambda f: f.endswith('.txt'), file_list):
    with open(file_name, 'r',encoding='utf-8') as file:
        # Read the contents of the file
        content = file.read()
        
        # Check if any number in the file contains a comma
        if "پدر" in content:
            print(file_name)
        
