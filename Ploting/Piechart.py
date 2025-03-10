import matplotlib.pyplot as plt 

# p=[70,59,80,75,80]

# socialmedia=['Instagram','Whatsapp','Facebook','Twitter','Reddit']

# plt.pie(p,labels=socialmedia,autopct='%1.1f%%',shadow=True)
# plt.title('Social Media Users')
# plt.show()



# a=[16,34,56,32,21]

# wateruse=['Faucet','Shower','Clothes Washer','Leaks','Other']

# plt.pie(a,labels=wateruse,autopct='%1.1f%%',shadow=True)
# plt.title('Water Uses In Place ')

# plt.show()


# population=[2,4,6,7,9,17,18,19]

# country=['Japan','Mexico','Bangladesh','Brazil','USA','India','China','Other']
# plt.pie(population,labels=country,autopct='%1.1f%%',shadow=True)
# plt.title('Population Of Pie Chart')
# plt.show()



water=[20,40,60,85]
n=len(water)
total=0
for x in water:
    total+=x
print(total)
percentage=[(x*100)for x in range(n)]
print(sum(percentage))
water=percentage
wateruse=['Toilet','Bathroom','Faucet','Leaks']

labels=[]
for i in range(n):
    labels.append('{0}  ({1})'.format(wateruse[i],water[i]))
print(labels)

plt.pie(water,labels=labels,autopct='%1.1f%%',shadow=True)
plt.show()