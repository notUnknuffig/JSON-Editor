import json
import os
import json_file_operations as json_file_op

possibleOperations = ['-show','-replace','-append', '-remove']
newStructList = ['-replace', '-append']

def main():
    op_type = input('Do you want to Create a new JSON-File or edit an already exsisting one? (create/edit) ')
    if(op_type == 'create'):
        print('Enter a path, where the JSON-file should be saved in.')
        create_path = input()
        if(os.path.isdir(create_path)):
            print('Enter a name for the file. (Do not enter a file extention!)')
            file_name = input()
            file_path = create_path + "\\" + file_name + ".json"
            new_file = None
            if(os.path.isfile(file_path)):
                if(input('The File already exsists in the Directory. Do you want to Overwrite it instead? (y/n) ') == 'y'):
                    new_file = open(file_path, 'w')
                else:
                    print('Programm will exit.')
                    return
            else:
                new_file = open(file_path, 'x')
            print('''----------------------------------------------------------
How to Format a Linear JSON-file:
   $ : creates an item that will be filled at the end of an operation.
   a,n[item] : creates a new array with n indecies and fills it with items.
   d{(key, item), (key, (a,n[item]))} : creates a new dict with key as key and item as value.
----------------------------------------------------------''')
            file_struct = input('Enter file structur: ')
            data = json_file_op.createStruct(json_file_op.parseStruct(file_struct))
            new_file.write(json.dumps(data, indent=4))
            new_file.close()
        else:
            print('File-Error 1: Path entered is incorrect or not a directory.')
    elif(op_type == 'edit'):
        edit_path = input('Enter a path to the JSON-File: ')
        if(os.path.isfile(edit_path)):
            with open(edit_path, 'r') as _file:
                try:
                    data = json.load(_file)
                except json.decoder.JSONDecodeError:
                    print('File-Error 3: JSON-Decode Error, File was loaded incorrectly or is empty.')
                    return
            print("""Enter a path to an element to edit:
----------------------------------------------------------
index: to select a specific item of an array,
$: to select all items in an array,
key: to select a specific value of a dict,
#: to select all items in a dict.
----------------------------------------------------------""")
            path = input()

            print("""Enter operation:
-append: to add an element to an array or dict,
-remove: to remove an element from an array or dict;""")
            operator = input()

            while operator not in possibleOperations:
                print('Operation-Error 4: Operation entered Incorrectly.')
                operator = input('Enter Operation again: ')
            _struct = ""
            if operator in newStructList:
                print(f"""Enter a Structure to {operator} the selected element: """)
                _struct = input()
            operation = [operator, _struct]

            data = json_file_op.getElement(path, data, operation)
            with open(edit_path, 'w') as _file:
               _file.write(json.dumps(data, indent=4))
        else:
            print('File-Error 2: Path entered is incorrect or not a file.')
    else:
        return

if __name__ == '__main__':
    main()