'''
Created on Dec 22, 2019

Read a text file into a list. 
Store the list in a set which removes duplicate words. 

@author: Shahriar
'''

def readFileAsList(filename):
    with open(filename, 'r') as file:
        filecontent = file.read()
        words = filecontent.split(" ")
        return words    
    
    
words = readFileAsList('paris.txt')

wordSet = set(words)

print(wordSet)
    

