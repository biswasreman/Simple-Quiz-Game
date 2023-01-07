player_name = input("What's your name ?\n> ").title()

print(f"Welcome to my Full Form Quiz Game {player_name}.")

start = input("Do you want to start the Game?\n> ").lower()

if start != "yes":
    quit()

print(f"Awesome {player_name} let's play :)")

score = 0

print("\n")

q = input("What's the full form of CPU?\n> ").lower()

if q == "central processing unit":
    score = score + 1
    print("correct!")
else:
    print("Incorrect!")


q = input("What's the full form of GPU?\n> ").lower()

if q == "graphics processing unit":
    score = score + 1
    print("correct!")
else:
    print("Incorrect!")


q = input("What's the full form of RAM?\n> ").lower()

if q == "random access memory":
    score = score + 1
    print("correct!")
else:
    print("Incorrect!")


q = input("What's the full form of IP?\n> ").lower()

if q == "internet protocol":
    score = score + 1
    print("correct!")
else:
    print("Incorrect!")



q = input("What's the full form of USB?\n> ").lower()

if q == "universal serial bus":
    score = score + 1
    print("correct!")
else:
    print("Incorrect!")


print("\n")    

print("You got", score, "Correct Answers.")

print("You got " + str((score / 4) * 100) + "%")

print("\n")





