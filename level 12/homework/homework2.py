num = 5
guess =int(input("Guess the number between 1 and 6: "))


if guess > 6:
    print("I said between 1 and 6!")
elif guess < 1:
    print("I said between 1 and 6!")

if num == guess:
    print("It's correct!")
else:
    print("it's incorrect!")


