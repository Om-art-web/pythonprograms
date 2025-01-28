import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,'g--',linewidth=22,label='y=2x')

plt.title('Line Plot Example')
plt.xlabel("X-Axis")              # (xlabel) makes x axis in Chart figure
plt.ylabel("Y-Axis")              # (ylabel) makes y axis in Chart figure
plt.legend()
plt.grid(True)                    # (Grid)   makes Grid in Chart figure 
plt.show()




# x=[2,3,4,5,6,8]
# y=[1,5,3,7,8,9]

# plt.plot(x,y,c='green',linewidth=1)
# plt.plot(y,x,c='green',linewidth=2)
# plt.scatter(x,y,c='purple',s=100,label='Data Points')
# plt.title("Scatter Plot Example")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.legend()
# plt.grid(True)
# plt.show()






