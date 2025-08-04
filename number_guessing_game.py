import random
logo='''
88b 88 88   88 8b    d8 88""Yb 888888 88""Yb          
88Yb88 88   88 88b  d88 88__dP 88__   88__dP          
88 Y88 Y8   8P 88YbdP88 88""Yb 88""   88"Yb           
88  Y8 `YbodP' 88 YY 88 88oodP 888888 88  Yb          
 dP""b8 88   88 888888 .dP"Y8 .dP"Y8 88 88b 88  dP""b8
dP   `" 88   88 88__   `Ybo." `Ybo." 88 88Yb88 dP   `"
Yb  "88 Y8   8P 88""   o.`Y8b o.`Y8b 88 88 Y88 Yb  "88
 YboodP `YbodP' 888888 8bodP' 8bodP' 88 88  Y8  YboodP
 dP""b8    db    8b    d8 888888                      
dP   `"   dPYb   88b  d88 88==                        
Yb  "88  dP__Yb  88YbdP88 88==                        
 YboodP dP""""Yb 88 YY 88 888888
 
 
 '''
 
 
 
print(logo)                                
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("too high")
        return turns-1
    elif user_guess<actual_answer:
        print("too low")
        return turns-1
    else:
        print(f"you got it. the answer is {user_guess}")
    

def difficulty():
    level=input("Choose a difficulty, type 'easy' or 'hard': ").lower()
    if level=='easy':
        return EASY_LEVEL_TURNS
    elif level=='hard':
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input, defaulting to easy mode")  
        return EASY_LEVEL_TURNS
        


def game():
    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 and 100")
    answer=random.randint(1,100)
    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts remaining")

        guess=int(input("Make a guess: "))

        turns=check(guess,answer,turns)
        if turns==0:
            print("you've ran out of attempts!")
            print(f"the correct answer is {answer}")

            return
        elif guess!=answer:
            print("Wrong answer,guess again")

game()


    
    

