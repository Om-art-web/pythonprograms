def push(st,value):
    st.append(value)

def pop(st):
    if len(st)==0:
        return None
    return st.pop()

def isempty(st):
    if len(st) <=0:
        return True
    return False


st=[]

word= "   Ommo   "
word = word.strip().lower()
print(word)
for ch in word:
    push(st,ch)


result="Palindrom"

for ch in word:
    outch=pop(st)
    if ch !=outch:
        result="Not Palindrom"
        break
print(result)
