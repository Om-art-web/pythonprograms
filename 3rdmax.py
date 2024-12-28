a,b,c=78,26,89
# # if else ladder
# if a>=b and a>=c:
#     max=a
# elif b>=c:
#     max=b
# else:
#     max=c
# print(max)


# nested else
if a>=b:
    if a>=c:
        max=a
    else:
        max=c
else:
    if b>=c:
        max=b
    else:
        max=c
print(max)



max=a
if b>max:
    max=b
if c>max:
    max=c
print(max)


if a<b or a<c:
    if b>=c:
        max=b
    else:
        max=c
else:
    max=a
print(max)

