
l = [1,2,4,0,8,67,54]                                       #Normal
print(l)
print("........................")



print('Smaller to greater')

                                    #Smaller To Greater 
l.sort()
print(l)

print("........................")
print('Greater to Smaller')

                                          #Greater To Smaller 
l.sort(reverse=True)
print(l)




            # Sorted Array

a = ["cat", "dog", "ball", "apple"]
print(a)
print('..................................')
a.sort()
print(a)
print('..................................')
a.sort(reverse=True)
print(a)
print('..................................')

a = ["cat", "dog", "ball", "apple"]
sortedarray = sorted(a)
print("Original Array ", a)
print("Sorted Array ", sortedarray)

reversesortedarray = sorted(a, reverse=True)
print("Reverse Sorted Array ", reversesortedarray)

print('//////////////////////////////////////////////////////')

a = ["cat", "dog", "ball", "apple"]
a.sort(key=len)
print(a)

print('.....................')
a.sort(key=len, reverse=True)
print(a)


