list1= [22,3,-4,0,8,78,7]



min=list1[0]
print(min)
for i in list1:
    if i<min:
        min=i
        print(min)
print("min=",min)


print('.......................................................')

for i in list1:
    if i>min:
        min=i
    print(min)
print('Maximum = ',min)
