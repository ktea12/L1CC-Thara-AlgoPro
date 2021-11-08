#Define a function that given the file name of a text will return all its 
#hapaxes. Make sure your program ignores capitalization.

import re

tibsfile = "D:/untitled2.py"

def hapaxes(tibsfile):
    mySnippet = open("D:/untitled2.py", "r")
    regex = '\w+'
    wordlist = re.findall(regex, mySnippet.read().lower())
    freq = {rep: 0 for rep in wordlist}
    
    for word in wordlist:
        freq[word] += 1
        
    for word in freq:
        if freq[word] == 1:
            print(word)
        
            
hapaxes("D:/untitled2.py")
