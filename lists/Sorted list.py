originallist = [1, 2, 4, 4, 4, 3, 1, 2, 3, 2, 1, 4, 6]

# sortedlist = sorted(set(originallist))

print("Sorted =", originallist)

print('...............................................................')

# list= [1,2,3,1,2,5,5,6,34,5,34] 4,4,4,4

sortedlist = sorted(originallist)
print('Second Sorted =', sortedlist)
n = len(sortedlist)
originallist.clear()
originallist.append(sortedlist[0])
print('Original  =', originallist)
for i in range(1, n):
    print("(",sortedlist[i-1], sortedlist[i],end=")")
    if sortedlist[i-1] != sortedlist[i]:
        originallist.append(sortedlist[i])

print(sortedlist)
print(originallist)
