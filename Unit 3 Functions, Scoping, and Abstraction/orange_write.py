new_lines = []
#Reading the file using with open()
with open('apple.txt') as f:
    for line in f:
        if 'apple' in line:
            new_lines.append(line.replace('apple','orange'))
        else:
            new_lines.append(line)
#writing into orange.txt
with open('orange.txt','w') as f:   
    f.writelines(new_lines)
