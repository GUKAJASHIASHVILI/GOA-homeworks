num = 5
guess =int(input("Guess the number between 1 and 10: "))


if guess > 10:
    print("I said between 1 and 10!")
elif guess < 1:
    print("I said between 1 and 10!")

while num != guess:
    print("It's incorrect!")
    break
else:
    print("It's correct!")
