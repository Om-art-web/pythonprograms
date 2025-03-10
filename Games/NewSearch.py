import numpy as nmp


def getNumber():
    x = nmp.random.random()
    x = x*8
    x = int(x+1)
    return x
print('You have only 3 chance')
chances=3
x=getNumber()
print(x)



while True:
        if chances<=1:
            print('Try Again')
            print(chances, " attempts remaining")
            break
    
        
        num=int(input('Enter number between 1 to 8 = '))
        
        
        if num==x:
            print('You Won the Game')
        if chances==2:
            print('300 Points')
        if chances==1:
            print('200 Points')
        if chances==0:
            print('100 points')
            break
        if num<x:
            print('More')
        else:
            print('Less')
chances=chances-1


