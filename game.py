import random

n = random.randint(1,100)
guesses = 0
a = -1
while a!=n:
    guesses +=1
    a = int(input("Guess the number: "))
    if a > n:
      print("Lower number please👇🔽 ")
      print("")
    elif a < n:
      print("Higher number pleas👆🔼 ")
      print("")
print(f"you have guessed the number in {guesses} attempts👍✅")

