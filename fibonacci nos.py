f=int(input('enter no. till which you want fibonacci series\n'))
a=0
b=1
print('series:\n0\n1')
for x in range(0,f):
    z=a+b
    a=b
    b=z
    print(z)
input('press ANY KEY to exit')    
    

