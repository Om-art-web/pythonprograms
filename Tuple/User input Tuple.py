d = dict()
while True:
    print('0-Exit, 1-Enter, 2-Search, 3-Show All')
    option = int(input('Read Option : '))

    if option == 0:
        break
    if option == 1:
        print('Enter Class And Roll No')
        classno = int(input('Enter the Class = '))
        rollno = int(input('Enter the Rollno = '))

        t = tuple([classno, rollno])
        name = input('Name : ')
        d[t]=name
    if option==2:
        print("Search")
        classno=int(input('Enter the class no = '))
        rollno=int(input('Enter the rollno = '))
        result=  d.get((classno,rollno))    
        print(result)  

    if option==3:
        print(d)

