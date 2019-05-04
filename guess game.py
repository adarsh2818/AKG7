from random import randrange
v=randrange(1,21)
g=int(0)
c=0
print("PC has chosen a number")
print('U have to guess the number between 1 and 20')
print('LETS GO!!')
while g!=v:
    g=int(input('type your guess : '))
    if g==v:
        break
    print("try again")
    c+=1
    if g<v+3 and g>v-3:
        print('it was too close!')
print('\n\nCORRECT!!')
print('No. of guesses you took : ',c+1)
print(v,' was the number')
input('press enter to exit')
        
        
    

 
