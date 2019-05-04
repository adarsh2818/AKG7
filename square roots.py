v=float(input('value for square root:\n'))
guess=0
prec=0.0001
while guess*guess!=v and guess*guess<=v:
    guess+=prec
print('ANSWER :\n ',guess)    
input('press ENTER to exit')        
    