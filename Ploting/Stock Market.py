import matplotlib.pyplot as plt 

x=[1,2,3,4,5]
n=len(x)
previousclosingprice=65
prices=[23,34,56,78,10]
print(prices[4])
y=[previousclosingprice for x in range(n)]
print(y)
if prices[4]>previousclosingprice:
    plt.plot(x,prices,c='green',linewidth=2,label='Current Price')
else:
    plt.plot(x,prices,c='red',linewidth=2,label='Current Price')
plt.plot(x,y,c='gray',linewidth=2,label='Previous Price')

plt.scatter(x,prices,c='Gray',linewidth=3,label='Points')
plt.title('Reliance Share')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)
plt.show()

