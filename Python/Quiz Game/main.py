score = 0

print("Welcome To The Quiz")

answer = input("Do You Want To Play The Game :")

if answer != "yes":
    quit()

question = input("What does GTA Stands for? ")
if question == "Grand Theft Auto":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question = input("What does Ram Stands for? ")
if question == "Random Access Memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question = input("What does CPU Stands for? ")
if question == "Central Processing Unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question = input("What does GPU Stands for? ")
if question == "Graphical Processing Unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You Scored " + str((score / 4) * 100) + "%")