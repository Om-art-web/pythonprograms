import matplotlib.pyplot as plt

# value1 = int(input('First Value = '))
# value2 = int(input('Second Value = '))
# value3 = int(input('Third Value =  '))
# value4 = int(input('Fourth Value = '))
# value5 = int(input('Fifth Value = '))


# values = [value1, value2, value3, value4, value5]
values = [2, 4, 6, 8, 10]
n = len(values)
base = ord('A')
labels = [ chr(base + x) + " (" + str(values[x]) + ")" for x in range(n)]
print(labels)
plt.pie(values,labels=labels)
plt.show()
