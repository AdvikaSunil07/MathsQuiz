# this a game containing maths questions

name=input("Enter your name: ")

print("Welcome to the maths quiz!!!",name.capitalize())

play=input("Do you wanna play?? :")

if play.lower() != "yes":
    quit()

print("LET'S BEGIN")

score=0

q1= input("Is 1 a prime number? ")

if q1.lower() == "no":
    print("CORRECT ANSWER")
    score+=2
else:
    print("OOPS! WRONG ANSWER")
    score-=1

q1= input("Which of the following is a pythagorean triplet?\nA.(3,4,5)\nB.(2,3,4)\nC.(7,8,9)\nD.(5,6,7)\n")

if q1.upper() == "A":
    print("CORRECT ANSWER")
    score+=2
else:
    print("OOPS! WRONG ANSWER")
    score-=1

q1= input("What is zero factorial? ")

if q1 == "1":
    print("CORRECT ANSWER")
    score+=2
else:
    print("OOPS! WRONG ANSWER")
    score-=1


q1= input("What is the full form of HCF? ")

if q1.lower() == "highest common factor":
    print("CORRECT ANSWER")
    score+=2
else:
    print("OOPS! WRONG ANSWER")
    score-=1

q1= input("What is the full form of LCM?  ")

if q1.lower() == "least common multiple":
    print("CORRECT ANSWER")
    score+=2
else:
    print("OOPS! WRONG ANSWER")
    score-=1

    print("Well done....now let's calculate your score")

    print("your score is ",score)
