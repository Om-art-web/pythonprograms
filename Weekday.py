  #    Find the weekday given the week day no
dayno=int(input('Enter the day number:  '))

# dayno=3
if dayno==1:
    dayname="monday"
elif dayno==2:
    dayname="tuesday"
elif dayno==3:
    dayname="wednesday"

elif dayno==4:
    dayname="thursday"
elif dayno==5:
    dayname="friday"
elif dayno==6:
    dayname="saturday"
elif dayno==7:
    dayname="sunday"
else: 
    dayname='Invalid'

print('Dayname is:  ',dayname)