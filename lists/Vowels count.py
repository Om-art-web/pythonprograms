def lastChar(s):
    return s[len(s) - 1]

def vowelsCount(s):
    vowels="AEIOUaeiou"
    count=0
    for v in s:
        if v in vowels:
            count+=1
    # print("k" in vowels)
    return count

a = ["animal", "layer", "train", "ship"]

a.sort(key=vowelsCount)
print(a)
# x=vowelsCount("Apple")
# print(x)

