x=input('sentence to count vowels and conso:' )
y=str(x)
vow=0
cons=0
for char in y:
    if char =='a' or char=='e' or char =='i' or char=='o' or char=='u':
      vow+=1
    else:
        cons+=1
print('vowels:',vow)
print('consonants:',cons)     
input("press ANY KEY to exit")  
        