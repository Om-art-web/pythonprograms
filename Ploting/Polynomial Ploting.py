import matplotlib.pyplot as plt

n = 11
x = [i for i in range(n)]

y = [i*i for i in x]
print(x, y)

plt.plot(x,y)
plt.scatter(x,y)
plt.show()
