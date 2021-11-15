#2.Numbering text file.

with open("D:/untitled2.py", "r") as input:
    lines = input.readlines()
    counter = 0
    for line in lines:
        if line != '\n':
                with open("D:/new.untitled2.py", 'a+') as output:
                    output.write((str)(counter)+'. ' (line.replace("\n","")))
                    counter += 1


#3.Calculate average word length of text file.

import re

text = open("D:/untitled2.py", "r")
word = re.split("\s", text.read())
length = re.findall("\w", text.read())
for length in word:
    avgw = sum(len(length))/len(word)
    print(f'This text has the average word length of {avgw} letters.')


#4.Sentence splitter.

import re
miyagi = open("D:/miyagi.py", "r")
splitter = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', miyagi)
for i in splitter:
    print (i)