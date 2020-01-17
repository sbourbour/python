'''
Created on Dec 17, 2019

@author: Shahriar
'''

sentence = input("Enter a string of words:")

words = sentence.split(" ")

words.reverse()

# Print has an optional end argument which defaults to newline
# but you can replace it with for eg. space
# This prints all the words on one line
for word in words:
    print(word, end=" ")


    
    
