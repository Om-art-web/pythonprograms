      #   Ruppes and paise


rupees=int(input('Enter ruppes: '))
paise=int(input('Enter paise:  '))
totalpaise=rupees*100+ paise
rupee=totalpaise//100
# paise=totalpaise%100
print("₹ ",rupee,".",paise)

'''
rupees=10, paise=250
totalpaise=1000 + 250=1250
1250/100= 12
1250%100=50
'''