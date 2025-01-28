import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
n = len(x)
previousclosingprice = 70
price1 = [21, 32, 43, 54, 69]
price2 = [32, 38, 54, 67, 78]

y = [previousclosingprice for x in range(n)]
print(y)
if price1[4] > previousclosingprice:
    plt.plot(x, price1, c='Green', linewidth='2', label='Price 1')
else:
    plt.plot(x, price1, c='Red', linewidth=2, label='Price 1')

if price2[4] > previousclosingprice:
    plt.plot(x, price2, c='Green', linewidth=2, label='Price 2')
else:
    plt.plot(x, price2, c='Red', linewidth=2, label='Price 2')

plt.plot(x, y, c='Black', linewidth=2, label='Previous Price')
plt.scatter(x, price1, c='Blue', linewidth=2, label='Points')
plt.scatter(x, price2, c='Purple', linewidth=2, label='Points')
plt.title('2 Sharing')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)
plt.show()
