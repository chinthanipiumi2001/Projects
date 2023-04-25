print("Welcome to my computer Quiz!")
playing= input("Do you want to play?")


if playing.lower() != "yes":
    quit()
    
print("Okay! Let's paly  :)")
score=0

answer= input("What does cpu stand for? ")
if answer.lower()== "central processing unit":
    print("correct!")
    score += 1

else:
    print("incorrect!")

answer= input("What does GPU standed for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1

else:
    print("incorrect!")

answer= input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1


else:
    print("incorrect!")

answer= input("What does PSU stand for? ")
if answer.lower()== "power supply":
    print("correct!")
    score += 1


else:
    print("incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")



