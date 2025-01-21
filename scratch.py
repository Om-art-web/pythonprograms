# list1= [1,2,'Same','Name',2,3]

# list2=[45,56]
# list1.extend(list2)
# print(list1)


# list3=[2,3,1,5,4]

# # list3.sort()
# # print('Ascending Order = ',list3)

# # list3.sort(reverse=True)
# # print('Descending Order',list3)

# list3.reverse()
# print(list3)

# list4=[1,10,4,3,['Song',['Name']]]
# print(list4)


# list5=['Song','Name','Sad','Hard']


# a=[word for word in list5 if word.startswith("S")]
# print(a)


# list6=['Song','Share']

# n1,n2=list6

# print('1st =',n1)
# print('2nd = ',n2)


positions = [0]
stockprices = [21, 23, 25, 87, 56, 69, 78, 87, 96]
n = len(stockprices)
for i in range(1, n):
    if stockprices[i-1] > stockprices[i]:
        a, b = stockprices[i-1], stockprices[i]
        # print(stockprices[i-1],stockprices[i],i-1,i)
        positions.append(i)
# print(positions)
m = len(positions)
for i in range(1, m):
    # print(positions[i-1],positions[i])
    start = positions[i-1]
    end = positions[i]
    part = stockprices[start:end]
    print(part)
