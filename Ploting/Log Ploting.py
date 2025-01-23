import matplotlib.pyplot as plt
import math
n=11
x=[i for i in range(1,n)]
y=[math.log(i) for i in x]
print(x,y)

plt.plot(x,y)
plt.scatter(x,y)
plt.show()