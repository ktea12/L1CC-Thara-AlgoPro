#Define a function that given the file name of a text will return all its 
#hapaxes. Make sure your program ignores capitalization.

import re

tibsfile = "D:/untitled2.py"

def hapaxes(tibsfile):
    mySnippet = open("D:/untitled2.py")
    wordlist = re.findall(mySnippet.read().lower(), mySnippet.read().strip(".,;"))
    freqs = {key: 0 for key in wordlist}
    
    for word in wordlist:
        freqs[word] += 1
        
    for word in freqs:
        if freqs[word] == 1:
            print(word)
        
            
hapaxes("D:/untitled2.py")