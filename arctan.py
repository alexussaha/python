import decimal 
print('Please, enter input, to find arctan!') 
decimal.getcontext().prec = 100 
x = decimal.Decimal(input()) 
arctx = decimal.Decimal(0) 
print('Thank you!') 
for n in range(0,100000000) : 
    arctx = decimal.Decimal(arctx) + decimal.Decimal(x**(2*n+1)*((-1)**n)/(2*n+1)) 
print('Your variable', arctx)
pi=decimal.Decimal(arctx)*decimal.Decimal(4)
print('Your variable', pi)
