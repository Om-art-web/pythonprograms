a = input("Please enter the number of a  ")

b = int(input("Please enter the number of b  "))

c = int(input("Please enter the number of c  "))
a = int(a)


print("Area of triangle")


# print("a,b,c", a, b, c)


s = (a+b+c)/2

# print(s)

area = s*(s-a)*(s-b)*(s-c)
area = area**.5

print("Area = ", area)
