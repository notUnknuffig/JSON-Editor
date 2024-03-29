import json
import os

class jsonObject:
    def __init__(self):
        self._json = "c"
        self.layers = 0



def getDeepestLayer(_json):
    pass

def parseStruct(_struct):
    i = 0
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
            for j in range(a_length):
                new_layer += _struct[i][0] + ':'
                
        print(new_layer, i)
        i += 1
        _json = _json.replace('c', new_layer)

    return _json

if __name__ == '__main__':
    print(parseStruct('a-10:d-3:key_a-*:key_b-*:key_b-*'))
