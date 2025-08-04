# 🎯 Number Guessing Game (Python)

Welcome to the **Number Guessing Game** – a fun Python-based CLI game where the computer picks a number between 1 and 100, and your goal is to guess it with limited attempts depending on the difficulty level!


---

## 🕹️ How It Works

- The program picks a random number between **1 and 100**.
- You choose a difficulty level:
  - 🟢 `easy` → 10 attempts
  - 🔴 `hard` → 5 attempts
- You keep guessing until:
  - You get the correct number, or
  - You run out of attempts.

The game tells you if your guess is **too high** or **too low** after each attempt.

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Clone this repo or copy the code into a `.py` file.


python number_guessing_game.py


---


🔧 Features

Difficulty levels (easy and hard)

Randomized number each game session

Feedback on whether guess is too high or too low

Attempt counter and graceful end message


---

🧠 Example Output


<pre>


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
 
 
 
Welcome to number guessing game!
I am thinking of a number between 1 and 100
Choose a difficulty, type 'easy' or 'hard': easy
you have 10 attempts remaining
Make a guess: 50
too high
Wrong answer,guess again
you have 9 attempts remaining
Make a guess: 37
too high
Wrong answer,guess again
you have 8 attempts remaining
Make a guess: 27
too high
Wrong answer,guess again
you have 7 attempts remaining
Make a guess: 20
too high
Wrong answer,guess again
you have 6 attempts remaining
Make a guess: 15
too high
Wrong answer,guess again
you have 5 attempts remaining
Make a guess: 10
too low
Wrong answer,guess again
you have 4 attempts remaining
Make a guess: 13
too high
Wrong answer,guess again
you have 3 attempts remaining
Make a guess: 11
too low
Wrong answer,guess again
you have 2 attempts remaining
Make a guess: 12
you got it. the answer is 12
  
</pre>

---

📂 File Structure


- number_guessing_game.py  # Main game script
- README.md                # Game documentation
