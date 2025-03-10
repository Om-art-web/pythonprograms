def push(st, value):
    st.append(value)


def pop(st):
    if len(st) == 0:
        return None
    return st.pop()


def isempty(st):
    if len(st) <= 0:
        return True
    return False


st = []
result = 'correct'
word = '(1-2)+(2-4)'

n = len(word)
# print(n)
for i in range(n):
    # print(i)
    ch = word[i]
    if ch == '(':
        push(st, i)
    if ch == ')':
        n = pop(st)
        part = word[n:i+1]
        print(part)
# print(st)
