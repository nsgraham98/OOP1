import os
file_name = input ('Enter file name: ')
confirm = input(f'You are about to delete the {file_name} file, are you sure? ')
if confirm.upper () == 'Y' or confirm.upper () == 'YES':
    os.remove(file_name)
    print (f'{file_name} is deleted')
elif confirm.upper () == 'N' or confirm.upper () == 'NO':
    print (f' {file_name} is not deleted')
else:
    print('Invalid input')
