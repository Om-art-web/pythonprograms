cricketers = {"A", "C","E"}
footballers = {"B", "C","E"}

u = cricketers.union(footballers)  # All elements with duplicates only once
print("Union ", u)

i = cricketers.intersection(footballers)  # Common elements only
print("Intersection ", i)

diff = cricketers.difference(footballers)  # Elements in cricketers but not in footballers
print("Difference ", diff)

print()

diff = cricketers - footballers  # Same as above
print("Difference ", diff)

symmdiff = cricketers.symmetric_difference(footballers)  # Remove common elements
print("Symmetric Difference", symmdiff)


print()

symmdiff = footballers.copy()
print("Symmetric Difference", symmdiff)