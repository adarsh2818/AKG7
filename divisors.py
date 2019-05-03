#finding all divisors of a number
x=int(input('enter a number:  '))
a=1
print('DIVISORS:')
while a<=x:
    if x%a==0:
        print(a)
        a+=1
    else:
            a+=1
input()
            