print('WELCOME TO MINI CALC\n')
print('ENTER TWO NUMBERS AND AN OPERATION TO PERFORM\n')
input('PRESS ANY KEY TO CONTINUE')
x=float(input('ENTER THE FIRST NUMBER:'))
y=float(input('ENTER THE SECOND NUMBER:'))
c=str(input("\n NOW GIVE OPERATION TO PERFORM (+,-,/,*):\n"))
print('RESULT:\n')
if c=='+' :
    print(x+y)
elif c=='-':
   print(x-y)
elif c=='*':
   print(x*y)
elif c=='/':
   print(x/y)
else:
    print('wrong operation')
input('press ANY KEY to exit')   