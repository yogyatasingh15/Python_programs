
# This is a mini game of Snake, Water and Gun 
# We import the random module to it 
import random 

def move(a,b):  # Function to generate the result  
    if a == 's':
        if b == 's' :
            return None
        elif b == 'w':
           return  False
        elif b == 'g':
           return  True
    elif a == 'w':
        if b == 's' :
            return True
        elif b == 'w':
            return None
        elif b == 'g':
            return False
    elif a == 'g':
        if b == 's' :
            return False
        elif b == 'w':
            return True
        elif b == 'g':
            return None
    
#  a = Computer's choice
#  b = User's choice

print("\n")
rand_num = random.randint(1,3)
print("Computer's turn : Snake(s), Water(w) , Gun(g)\n")

if rand_num == 1:
    a = 's'
elif rand_num == 2:
    a = 'w' 
elif rand_num == 3:
    a = 'g'

b  = input("Players's turn : Snake(s), Water(w) , Gun(g)\n")
print("computer's choice: " )
ret = move(a, b)
if ret == False:
    print("Sorry You lose the Game")
elif ret == True:
    print("Bravo! You Won the Game")
elif ret == None:
    print("The game is tie")


