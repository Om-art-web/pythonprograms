positions = [0]
stock = [1, 5, 7, 8, 4, 3, 9]
n = len(stock)
for i in range(1, n):

    a, b = stock[i-1], stock[i]
    if stock[i] > stock[i-1]:
        print(a, b)
        positions.append(i)

m = len(positions)

for i in range(1, m):

    start = positions[i-1]
    end = positions[i]
    part = stock[start:end]
    print(part)



