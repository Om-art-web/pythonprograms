import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,linewidth=2,label="Nothing")

plt.title("Line Plot Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True)
# plt.show()
n=0
plt.savefig("videopics/graph{0}.png".format(n))
n+=1


 # Second


n=11

x=[i for i in range(n)]
print(x)

y=[7 for i in x]

print(y)

plt.plot(x,y)
plt.scatter(x,y)
# plt.show()
n=1
plt.savefig("videopics/graph{0}.png".format(n))
n+=1

import math

n=12

x=[i for i in range(1,n)]
y=[math.log(i)for i in x]
print(x,y)

plt.plot(x,y)
plt.scatter(x,y)
# plt.show()
n=2
plt.savefig("videopics/graph{0}.png".format(n))
n+=1





