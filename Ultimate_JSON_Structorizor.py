import json
import os

global json_file

def findObject(file_data):
    print("Enter the path to what should be changed. Use a number for indexes and * for all indexes of an array. Use a string for a key and $ for all keys of a dictionary.")
    value_path = input("Enter a value path: ").split()
    if "*" in value_path or "$" in value_path:
        pass
    else:
        try:
            pass
        except (IndexError, ValueError):
            pass
        except (IndexError, ValueError):
            pass

def main():
    print("JSON-File Structorizor:")
    file_path = input("Enter a file path, if the file path is a directory, create a json file within it: ") 
    if os.path.isfile(file_path):
        json_file_path = file_path
    elif os.path.isdir(file_path):
        filename = input("Enter the filename (without extension): ")
        if not filename:
            print("Filename cannot be empty.")
            return
        
        json_file_path = os.path.join(file_path, f"{filename}.json")
        if os.path.exists(json_file_path):
            print(f"A file with the name '{filename}.json' already exists in the directory.")
            return
        
        print(f"JSON file '{filename}.json' created in '{file_path}'.")
    else:
        print("Provided file path is not a directory.")
        return

    with open(json_file_path, 'r') as json_file:
            file_data = json.load(json_file)

    findObject(file_data)

    # Create new JSON structure input: "array int_len" -> Input: "dict key_1 key_2 key_3..."
    # Add key blah blah blah...
    # Add Value input: {Type} str {Value} Hallo Welt! ; {Type} array {Array-Type} str 'item_1' 'item_2' 'item_3' 'item_4'... ; {Type} num 257.5125
    print("Possible Operations: 'create'-> Create a new JSON structure; 'add-key' -> add a new key to an exsisitng dictionary; 'fill-value' -> set a new value for a given key; get_struct shows all the structure of the Json file.")

if __name__ == __name__:
    main();