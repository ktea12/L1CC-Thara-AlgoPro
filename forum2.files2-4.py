#Numbering text file.

with open("D:/untitled2.py", "r") as input:
    lines = input.readlines()
    counter = 0
    for line in lines:
        counter += 1
        if line != '\n':
                with open("D:/new.untitled2.py", 'a+') as output:
                    output.write(f'{counter}. {line.replace("/n","")}')


#Calculate average word length of text file.

import re

text = open("D:/untitled2.py", "r")
word = re.split("\s", text.read())
length = re.findall("\w", text.read())
for length in word:
    avgw = sum(len(length))/len(word)
    print(f'This text has the average word length of {avgw} letters.')


#Sentence splitter.
