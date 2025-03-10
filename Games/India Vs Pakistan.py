import matplotlib.pyplot as plt


india = []
pakistan = []
overs = 5
# x=[x+1 for x in range(overs)]
x=[]
x2=[]
for over in range(overs):
    print('enter run for over no', over+1)
    run = int(input('='))
    if over==0:
        india.append(run)
    else:
        india.append(india[-1] + run)
    x.append(over+1)
    print(india)

for over in range(overs):
    print('enter run for pakistan over no',over+1)
    runs=int(input('== '))
    if over==0:
        pakistan.append(runs)
    else:
        pakistan.append(pakistan[-1]+runs)
    x2.append(over+1)
    print(pakistan)

plt.plot(x,india,linewidth=3,label='India',c='Blue')
plt.plot(x2,pakistan,linewidth=2,label='Pakistan',c='Green')
plt.scatter(x,india,c='lightcoral')
plt.scatter(x2,pakistan,c='purple')
plt.title('Cricket Match Score ')
plt.xlabel('Runs')
plt.ylabel('Overs')
plt.legend()
plt.grid(True)
plt.show()