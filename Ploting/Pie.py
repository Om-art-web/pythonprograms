import matplotlib.pyplot as plt

value1 = int(input('First Value = '))
value2 = int(input('Second Value = '))
value3 = int(input('Third Value =  '))
value4 = int(input('Fourth Value = '))
value5 = int(input('Fifth Value = '))


values = [value1, value2, value3, value4, value5]
labels=[str(x) for x in values]
plt.pie(values,labels=labels)
plt.show()
