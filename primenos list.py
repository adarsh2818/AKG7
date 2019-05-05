def cpn(a):
  x=2
  while x<a:
    if a%x==0:
        break
    else:
        x+=1
        if x==a-1:
            print(a)

def main():            
  c=1    
  n=int(input('ENTER NO. TILL WHICH YOU WANT PRIME NOS. : '))         
  while c<=n:
      cpn(c)
      c+=1
  print('done')      
  input()

main()
            