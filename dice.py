from random import randrange
value=randrange(1,6)
input('PRESS ENTER TO ROLL DICE')
print('+----------+')
if value==1:
     print('|          |')
     print('|    *     |')
     print('|          |')
elif value==2:
     print('|*         |')
     print('|          |')
     print('|         *|')
elif value==3:
     print('|*         |')
     print('|    *     |')
     print('|         *|')
elif value==4:
     print('|*        *|')
     print('|          |')
     print('|*        *|')
elif value==5:
     print('|*        *|')
     print('|    *     |')
     print('|*        *|')
elif value==6:
     print('|*   *   *|')
     print('|         |')
     print('|*   *   *|')
print('+----------+')
                    
input()