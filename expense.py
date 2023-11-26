print('Expense Recording System')

others=[]
others_Rs=[]
Groceries=[]
travelling=[]
movies=[]

def main():
 b=0
 c=0
 d=0
 e=0
 x=0
 y=0
 
 print('choice any one of category:- ')
 print("1. Groceries ")
 print('2. travelling')
 print('3. movies')   
 print('4. others') 
 a= int(input("enter the number (1-4):"))

 if a==1:
 
     b= int(input('enter the amount you spend in Groceries:-'))
     Groceries.append(b)
   
 
 elif a==2:

     c=int(input('enter the amount you spend in travelling:-'))
     travelling.append(c)
     
 elif a==3:
 
     d=int(input('enter the amount you spend in movies:-'))
     movies.append(d)
     
 elif a==4:

       x=int(input('enter the number of category you want to make :-  '))
       y=0
       
 while y<x: 
     
     f=str(input('enter the name of category in which you have spend money :-'))
     others.append(f)
     e=int(input('enter the amount you spend in above category :-'))
     others_Rs.append(e)
     y=y+1
  
  
 more=str(input( 'add more expense(yes/no):-').lower())
 if more=='yes':
     main()
     
 else:
     
    z=0
    p=0
    t=0
    gr=0
    tr=0
    mo=0
    
    print('your total expense:-') 
    print('Groceries-{}'.format(Groceries))
    print('travelling-{}'.format(travelling))
    print('movies-{}'.format(movies))
    
    while z<x:
        print('{}-{}'.format(others[z],others_Rs[z]))
        t=t+others_Rs[z]
        z=z+1
        
    gr=sum(Groceries)
    tr=sum(travelling)
    mo=sum(movies)
    p=gr+tr+mo+t
    print('total amount you spend:-{}'.format(p))
     
main() 
    

     
  

 
