import matplotlib.pyplot as plt

salesman = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testscore = [40, 70, 50, 60, 80, 50, 90, 40, 60, 60]
sales = [2.5, 6.0, 4.5 ,5.0, 4.5, 2.0, 5.5, 3.0, 4.5, 3.0,]
print(salesman, testscore, sales)


a = sum(salesman)
b = sum(testscore)
c = sum(sales)
print('Sum = ', a)
print('Sum = ', b)
print('Sum = ', c)

avg = a/len(salesman)

print('Average = ', avg)


# plt.plot(salesman, testscore, c='purple', label='Salesman')
# plt.scatter(salesman, testscore, c='lightcoral', label='TestScore')
# plt.title('Score')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.grid(True)
# plt.show()

n = len(testscore)
# print('Length :',n)
# print()
assumedmean = 60
assumedaverage = 4.5
for index in range(n):
    dx = testscore[index]-assumedmean
    dy = sales[index]-assumedaverage
    print(testscore[index], "\t", sales[index],
          "\t", dx, "\t", dy, "\t", dx*dy,"\t",dx*dx,"\t",dy*dy)
    
