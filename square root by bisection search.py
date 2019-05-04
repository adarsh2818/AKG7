v=float(input('enter value for square root : \n'))
low=0.0
high=v
guess=(low+high)/2.0
while abs(guess**2.0-v)>=0.0001:
    if guess**2.0>v:
        high=guess
        guess=(low+high)/2.0
    else :
        low=guess
        guess=(low+high)/2.0
print('answer is close to : ',guess)
input('press enter to exit')        

        
          
