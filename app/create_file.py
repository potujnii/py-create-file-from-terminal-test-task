from datetime import datetime
from sys import argv
from os import mkdir, chdir

filename = 'file.txt'
directories = []

if '-f' in argv:
    index = 0
    for i in range(len(argv) - 1):
        index += 1
        if argv[i: i + 1] == ['-f']:
            break
    filename = argv[index]

    if "-d" in argv:
        index2 = 0
        for i in range(len(argv) - 1):
            index2 += 1
            if argv[i: i + 1] == ['-d']:
                break
        directories = argv[index2:index - 1]

elif '-d' in argv:
    index = 0
    for i in range(len(argv) - 1):
        index += 1
        if argv[i: i + 1] == ['-d']:
            break
    directories = argv[index:len(argv)]


file_data = [str(datetime.now()), "\n"]

while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    file_data.extend([line + '\n'])

for directory in directories:
    try:
        mkdir(directory)
    except Exception as e:
        print(e)
    chdir(directory)

with open(filename, "w") as f:
    f.writelines(file_data)
