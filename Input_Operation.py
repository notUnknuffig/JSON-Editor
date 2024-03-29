import json
import os
import Create_JSON_File as c_json_file
import Edit_JSON_File as e_json_file


def main():
    op_type = input('Do You want to create a new JSON-file? (y/n) ')
    if(op_type == 'y'):
        print('Enter a path, where the JSON-file should be saved in.')
        create_path = input()
        if(os.path.isdir(create_path)):
            print('Enter a name for the file. (Do not enter a file extention!)')
            file_name = input()
            file_path = create_path + "\\" + file_name + ".json"
            print(file_path)
            if(os.path.isfile(file_path)):
                if(input('The File already exsists in the Directory. Do you want to Overwrite it instead? (y/n) ') == 'y'):
                    new_file = open(file_path, 'w')
                else:
                    print('Programm will exit.')
                    return
            else:
                new_file = open(file_path, 'x')
            print("""* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                    *                                                                                       *
                    *	How to Format a JSON-file:                                                          *
                    *	* : creates an item that will be filled at the end of an operation.                 *
                    *	a(n, item) : creates a new array with n indecies and fills it with items.           *
                    *	d('key_a':item 'key_b':item) : creates a new dict with key as key and               *
                    *                                  item as value.                                       *
                    *                                                                                       *
                    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *""")
            file_struct = input('Enter file structur: ')
            print(c_json_file.parseStruct(file_struct))
        else:
            print('File-Error 1: Path entered is incorrect or not a directory.')
    elif(op_type == 'n'):
        edit_path = input('Enter a path to the JSON-File')
        if(os.path.isfile(create_path)):
            print('Opening File!')

    else:
        return

if __name__ == '__main__':
    main();