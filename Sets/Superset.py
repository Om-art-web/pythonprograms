a={1,2,3,4,5}
b={1,2,3}

print('Superset : ',a.issuperset(b))
print("superset = ",a>=b)

print(".................................")

print("Superset ", b.issuperset(a))
print("Superset ", b >= a)