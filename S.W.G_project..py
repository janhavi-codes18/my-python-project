import random
'''
1 for snakew
-1 for water
0 for gun

'''
computer =random.choice([-1,0,1])
youstr = input("enter you choice : ")
youdict = {"s":1,"w":-1,"g":0}
reversedict= {1:"snake",-1:"water",0:"Gun"}

you = youdict[youstr]

print(f"you chose{reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("its draw !")
else:
    
    if(computer==-1 and you ==1):
      print("you win")
    elif(computer ==-1 and you ==0):
       print("you lose")
    
    elif(computer ==1 and you ==-1):
       print("you lose")
    
    elif(computer ==-1 and you ==0):
       print("you lose")
    
    elif(computer ==0 and you ==-1):
       print("you lose")
    
    elif(computer ==0 and you ==1):
       print("you lose")
    else:
       print("something went wrong")

# this is short method of the this project
'''if((computer-you)==-1  or (computer-you)==2):    
         print("you lose"!)
   else:
          print("you win" !)
          
'''