import time
x=time.time()
n=float(input('set timer : '))
y=time.time()-x
while y<=n:
    y=time.time()-x
print('time complete , stop')
input()    