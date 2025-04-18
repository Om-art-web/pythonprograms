import matplotlib.pyplot as plt

n=11

x=[i for i in range(n)]
print(x)

y=[7 for i in x]    
print(y)

plt.plot(x,y)
plt.scatter(x,y)
plt.show()
