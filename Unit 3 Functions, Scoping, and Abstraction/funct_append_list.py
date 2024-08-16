# append to a list
# does not need return bc its a list
def append_to_list(names_list, name):
    names_list.append(name)

names = ['Fred', 'John']
new_name = 'Ed'

append_to_list(names, new_name)
append_to_list(names, 'Andy')
print (names)
