no1=input("Enter First Name:")
no2=input("Enter Second Name:")
score=0
for character in no1:
     if character in 'aeiou':
         score+=20
     if character in 'friend':
        score+=5
for character in no2:
    if character in 'aeiou':
        score+=20
    if character in 'friend':
        score+=5
if(score>20) and score<60:
    print("Your Score is",score,"And You are Friends")
elif(score>60) and score<100:
    print("Your Score is",score,"And You are Good Friends")
elif(score>100):
    print("Your Score is",score,"And You are Best Friends")
