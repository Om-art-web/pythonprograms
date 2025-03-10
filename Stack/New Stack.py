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
result='correct'
word = '(1+2)+(2+4)('
for ch in word:
    if ch =='(':
        # print(ch)
        push(st,ch)
    if ch ==')':
        if isempty(st):
            result='wronng'
            break
        else:
            pop(st)
if not isempty(st):
    result='wrong'
print(result)
