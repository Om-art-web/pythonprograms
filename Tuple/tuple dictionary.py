#   Create a dictionary with a tuple(classname,rollno) as key and name as value.


classname = int(input('Enter the classno : '))
rollno = int(input('Enter the rollno'))
d = dict()
t = tuple([classname, rollno])
print(t, type(t))

name = input('enter the name : ')
d[t] = name
print(d)
print(d[t])
