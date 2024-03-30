def string_to_nested_list(string):
    nested_list = []
    stack = []
    current_string = ''

    for char in string:
        if char == '[':
            if current_string:
                nested_list.append(current_string)
                current_string = ''
            stack.append(nested_list)
            nested_list = []
        elif char == ']':
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

if __name__ == "__main__":
    input_string = input("Enter the string to convert to a nested list: ")
    result = string_to_nested_list(input_string)
    print("Resulting nested list:")
    print(result)
