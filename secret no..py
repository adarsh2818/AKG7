print("Please think of a number between 0 and 100!")
#GIVE HINTS FOR GUESS: h=high, l=low, c=correct
input('PRESS ENTER TO START')
hi=100
lo=0
flag=0
guess=(hi+lo)/2
while flag==0:
    guess=(hi+lo)//2
    print('is your secret no. ',guess,' ?')
    n=str(input('your hint :'))
    if n=='c':
        flag=1
    elif n=='h':
        hi=guess
    elif n=='l':
        lo=guess
    else:
        print('wrong input')
print('GAME OVER. YOUR SECRET NO. IS ',guess)
input('enter to exit')       
        
    
    