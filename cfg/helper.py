def str_transform(string: str):
    st_list = string.split(', ')
    return st_list


string = input('Enter string: ')
print(str_transform(string))
