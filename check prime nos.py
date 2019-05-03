a=int(input('ENTER A NUMBER TO CHECK IF IT IS PRIME OR NOT:\n'))
x,z=2,1
while x<a:
    if a%x==0:
        print("NOT PRIME")
        break
    else:
        x+=1
        if x==a-1:
            print("PRIME")
input('press ENTER to exit')
            
            
        