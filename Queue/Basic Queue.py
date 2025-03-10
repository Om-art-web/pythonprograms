def enque(queue,data):
    queue.insert(0,data)
    print(queue)

def deque(queue):
    if len(queue)==0:
        return None
    x= queue.pop()
    return x
def isempty(queue):
    if len(queue)==0:
        return True
    return False



a= []

while True:
    print("0- Exit, 1-Insert, 2-Deque, 3-Show,")

    option=int(input('Read option : '))

    if option==0:
        break
    if option==1:
        user=input('Enter Value : ')
        enque(a,user)
    if option==2:
        x=deque(a)
        print(x)
    if option==3:
        print(a)

    

