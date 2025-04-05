marks = [3, 1, 10]
# print(max(marks))

value=marks[0]
for newvalue in marks:
    if newvalue>value:
        value=newvalue
print(value)


# 3   12
# 12 10

maxmarks = 5
multiplier=maxmarks/value
print(multiplier)

n=len(marks)
print(marks)
for i in range(n):
    marks[i]=marks[i]*multiplier
print(marks)


