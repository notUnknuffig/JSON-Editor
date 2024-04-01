import json
import os

def replaceData(data, path, replaceChar):
    if isinstance(data, dict):
        for key, value in data.items():
            path.append(key)
            if isinstance(value, str) and replaceChar in value:
                _input = input(f"Enter replacement for '{value}' at {path}: ")
                if len(_input) >= 0:
                    _input = "/"
                data[key] = value.replace(replaceChar, _input)
                path.pop()
            else:
                data[key] = replaceData(value, path, replaceChar)
        if len(path) > 1:
            path.pop()
    elif isinstance(data, list):
        for i, item in enumerate(data):
            path.append(i)
            if isinstance(item, str) and replaceChar in item:
                _input = input(f"Enter replacement for '{item}' at {path}: ")
                if len(_input) >= 0:
                    _input = "/"
                data[i] = item.replace(replaceChar, _input)
                path.pop()
            else:
                data[i] = replaceData(item, path, replaceChar)
        if len(path) > 1:
            path.pop()
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
    elif _struct[0] == '"' and _struct[-1] == '"':
        part = _struct
    else:
        part = '"$"'
    return part


def createStruct(_struct):
    _json = createPartStruct(_struct)
    l_json = json.loads(_json)
    l_json = fillData(l_json, "$")
    return l_json


def executeOperation(operation, data):
    if operation[0] == '-show':
        print(data)
    elif operation[0] == '-replace':
        print(f"Replace {data} with: {operation[1]}")
        if operation[1][0] == '#':
            operation[1] = operation[1][1:]
            data = createStruct(parseStruct(operation[1]))
        else:
            data = operation[1]
    elif operation[0] == '-append':
        if isinstance(data, list):
            if operation[1][0] == '#':
                data.append(createStruct(parseStruct(operation[1][1:])))
            else:
                data.append(operation[1])
        elif isinstance(data, dict):
            if operation[1][0] == '#':
                new_data = parseStruct(operation[1][1:])
                if isinstance(new_data[0], str):
                    data[new_data[0]]  = createStruct(new_data[1])
                else:
                    data[input('Missing Key: Enter a key: ')] = createStruct(new_data)
            elif operation[1][0] == '-':
                _input = input(f'Enter Value for {[operation[1][1:]]} in {data}: ')
                if len(_input) > 0: 
                    data[operation[1][1:]] = _input
                else:
                    data[operation[1][1:]] = "/"
        elif isinstance(data, str):
            data += operation[1]
    return data


def getSubElement(_index, data, operation):
    if _index == '':
        data = executeOperation(operation, data)
        return data
    for i in range(len(_index)):
        if str(_index[i]).isnumeric() and isinstance(data, list):
            if(i > len(_index) - 1):
                data[int(_index[i])] = executeOperation(operation, data[int(_index[i])])
            else:
                data[int(_index[i])] = getSubElement(_index, data[int(_index[i])], operation)

        elif _index[i] == "$" and isinstance(data, list):
            for j in range(len(data)):
                if(i > len(_index) - 1):
                    data[j] = executeOperation(operation, data[j])
                else:
                    data[j] = getSubElement(_index, data[j], operation)
                
        elif _index[i] in data and isinstance(data, dict):
            if(i == len(_index) -1):
                data[_index[i]] = executeOperation(operation, data[_index[i]])
            else:
                data[_index[i]] = getSubElement(_index, data[_index[i]], operation)

        elif _index[i] == '#' and isinstance(data, dict):
            keys = data.keys()
            for key in keys:
                if(i == len(_index) -1):
                    data[key] = executeOperation(operation, data[key])
                else:
                    data[key] = getSubElement(_index, data[key], operation)
    return data


def getElement(_index, data, operation):
    _index = _index.split(" ")
    data = getSubElement(_index, data, operation)
    return data
