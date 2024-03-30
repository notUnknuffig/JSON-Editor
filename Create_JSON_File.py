import json
import os

def replaceData(data, path, replaceChar):
    if isinstance(data, dict):
        for key, value in data.items():
            path.append(key)
            if isinstance(value, str):
                data[key] = value.replace(replaceChar, input(f"Enter replacement for '{value}' at {path}: "))
                path.pop()
            else:
                data[key] = replaceData(value, path, replaceChar)
        if len(path) > 1:
            path.pop()
    elif isinstance(data, list):
        for i, item in enumerate(data):
            path.append(i)
            if isinstance(item, str):
                data[i] = item.replace(replaceChar, input(f"Enter replacement for '{item}' at {path}: "))
                path.pop()
            else:
                data[i] = replaceData(item, path, replaceChar)
        if len(path) > 1:
            path.pop()
    print(data)
    return data

def fillData(_json, replaceChar):
    replaceData(_json, [], replaceChar)
    return _json

def parseStruct(_struct):
    _struct = _struct.replace(" ", "")
    nested_list = []
    stack = []
    current_string = ''

    for char in _struct:
        if char == '[' or char == '{' or char == '(':
            if current_string:
                nested_list.append(current_string)
                current_string = ''
            stack.append(nested_list)
            nested_list = []
        elif char == ']' or char == '}' or char == ')':
            if current_string:
                nested_list.append(current_string)
                current_string = ''
            if stack:
                parent_list = stack.pop()
                parent_list.append(nested_list)
                nested_list = parent_list
        elif char == ',':
            if current_string:
                nested_list.append(current_string)
                current_string = ''
        else:
            current_string += char

    if current_string:
        nested_list.append(current_string)

    #print(nested_list)
    return nested_list

def createPartStruct(_struct):
    part = ""
    if _struct[0] == 'a':
        part += '['
        if str(_struct[1]).isnumeric():
            for i in range(int(_struct[1])):
                part += 'c,'
            part = part[:-1]
            part += ']'
            part = part.replace('c', createPartStruct(_struct[2]))
        else:
            print(_struct[1])
            for item in _struct[1]:
                part += createPartStruct(item) + ','
            part = part[:-1]
            part += ']'
        
    elif _struct[0] == 'd':
        part += '{'
        for key in _struct[1]:
            part += '"' + key[0] + '":' + createPartStruct(key[1]) + ','
        part = part[:-1]
        part += '}'
    else:
        part = '"*"'
    return part


def createStruct(_struct):
    _json = createPartStruct(_struct)
    l_json = json.loads(_json)
    l_json = fillData(l_json, "*")
    return l_json


if __name__ == '__main__':
    _json = createStruct(parseStruct(input()))
 #   _json = createStruct()
    print(_json)
