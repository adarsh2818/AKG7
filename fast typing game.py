import time
print('###HOW FAST CAN YOU TYPE###')
print('TYPE AND TIME TAKEN WILL NE SHOWN :\n')

print('PLAYER ONE ENTER AND START TYPING :\m')
input()
x=time.time()
input()
y=time.time()
z=y-x
print('PLAYER TWO ENTER AND START TYPING :\m')
input()
x=time.time()
input()
y=time.time()
t=y-x
if t==z:
    print('ohhhh....ITS A TIE!!!')
if t>z:
    print('\n\n      PLAYER 2 WINS!!')
else:
    print('\n\n      PLAYER 1 WINS!!')
print('\nPLAYER 1 TIME : ',z)
print('\nPLAYER 2 TIME : ',t)
print('\nTIME DIFFERENCE : ',abs(z-t))    
input()