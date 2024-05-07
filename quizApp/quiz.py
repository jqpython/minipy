print("Welcome to Quiz")

playing = input("Are you ready?")

if playing != "yes":
    quit()

print("Let's start")
score = 0
answer = input("What does RAM stand for? ").lower()
print(answer)

if answer == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")

total = print(f"Your total score is: {score}")
