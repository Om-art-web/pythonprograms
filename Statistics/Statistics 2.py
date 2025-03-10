x=[21,23,30,54,57,58,72,78,87,90]
y=[60,71,72,83,110,84,100,92,113,135]

a=sum(x)
b=sum(y)

print('Sum of X = ',a)
print('Sum of Y = ',b)

avg= a/len(x)
avg2=b/len(y)

print('Average X = ',avg,"\t",'Average Y = ',avg2)


# import matplotlib.pyplot as plt 
# plt.plot(x,y,c='Green',label='X')
# plt.scatter(x,y,c='Grey',label='Y')
# plt.title('Header')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.grid(True)
# plt.show()


n=len(x)
x2=[1089,961,576,0,9,16,324,576,1089,1296]
y2=[1600,841,784,289,100,256,0,64,169,1225]

for index in range(n):
    print(x[index],"\t",x2[index],"\t",y[index],"\t",y2[index],"\t",y[index]-x[index],"\t",x[index]-y[index])