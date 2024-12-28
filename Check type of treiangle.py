

   #  TYpe of trinangle 



a=int(input('First side:  '))
b=int(input('Second side:  '))
c=int(input('Third side:   '))

if  a==b==c:
    
    print("Triangle is equilateral")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")   


if  a+b>c and b+c>a and c+a>=b:

    print("The Triangle is:", triangle_type(a,b,c)) 

else:
    print("The side do not form a valid triangle.")   
    
    
