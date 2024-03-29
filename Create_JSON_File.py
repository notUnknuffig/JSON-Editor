import json
import os

def fillData(_json):
    return _json

def parseStruct(_struct):
    i = 0
    _struct = _struct.replace(" ", "")
    _struct = _struct.replace("[", ":")
    _struct = _struct.replace("{", ":")
    _struct = _struct.split(':')
    for char in range(len(_struct)): 
        _struct[char] = _struct[char].split('-')
    print(_struct)
    _json = 'c' #c = Current

    while i < len(_struct): 
        new_layer = ""
        if(_struct[i][0] == 'a'):
            new_layer = '['
            a_length = int(_struct[i][1])
            for j in range(a_length):
                new_layer += 'c,'
            new_layer = new_layer[:-1]
            new_layer += ']'

        elif(_struct[i][0] == 'd'):
            new_layer = '{'
            d_length = int(_struct[i][1])
            i += 1
            for j in range(d_length):
                new_layer += '"' + _struct[i][0] + '":'
                new_sub_layer = ""
                if(_struct[i][1] == 'a'):
                    new_sub_layer = '['
                    sub_a_length = int(_struct[i][2])
                    for jj in range(sub_a_length):
                        new_sub_layer += '"r",'
                    new_sub_layer = new_sub_layer[:-1]
                    new_sub_layer += '],'
                else:
                    new_sub_layer = '"*",'
                new_layer += new_sub_layer
                i += 1
            new_layer = new_layer[:-1]
            new_layer += '}'
        else: 
            new_layer = '"*"'
        i += 1
        _json = _json.replace('c', new_layer)
        _json = fillData(_json)
    l_json = json.loads(_json)
    return l_json

if __name__ == '__main__':
    _json = parseStruct(input())
    print(_json)
