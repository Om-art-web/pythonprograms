import matplotlib.pyplot as plt 
data=[]
labels=[]
colors=[]

while True:
    print('0-Break, 1-Enter Data, 2-Show Pie Chart')
    option=int(input('Read Option : '))

    if option==0:
        break
    if option==1:
        print('Enter Data For Pie Chart')
        Data1=int(input('=> '))
        Data2=int(input('=> '))
        Data3=int(input('=> '))

        data.extend([Data1,Data2,Data3])
        labels.extend(['A','B','C'])
        colors.extend(['Pink','Lightblue','Lightcoral'])

    if option==2:
        plt.pie(data,labels=labels,colors=colors,shadow=True,autopct='%1.1f%%')
        plt.show()
