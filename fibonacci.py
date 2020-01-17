'''
Created on Dec 15, 2019

@author: Shahriar
'''

def generateFibonacci(count):
    fibonacciList = []
    i = 0
    while i < count:
        if i == 0:
            fibonacciList.append(1)
        elif i == 1:
            fibonacciList.append(1)
        else:
            fibonacciList.append(fibonacciList[i-1] + fibonacciList[i-2])            
        i += 1        
    return fibonacciList
        
        
count = input("Please enter how many Fibonacci numbers to generate:")

fibonacciList = generateFibonacci(int(count))

print(fibonacciList)