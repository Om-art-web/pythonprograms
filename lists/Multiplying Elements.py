# a=[1,2,3,4]

# mul=1

# for i in a :   mul=mul*i
# # print(a)

# print('Multiplication is:  ',mul)

# print('................................................')


runs = [1, 10, 23, 34, 56]
names = ["Sachin", "Rahul", "Mahender", "Sourav", "Saubhagya"]
newdict1 = {name: run for (name, run) in zip(names, runs)}
print(newdict1)
print('................................................................')


newdict2 = {run: name for (run, name) in zip(runs, names)}
print(newdict2)
print('................................................................')


newdict3 = {run: name for (run, name) in zip(runs, [run * 2 for run in runs])}
print(newdict3)

print('.................................................................')

newdict4 = {run: name for (run, name) in zip(runs, [(lambda run: run + 2)(run) for run in runs])}
print(newdict4)