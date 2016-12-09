__author__ = 'jc450453'

score=float(input("Enter score: "))
if(score<0 and score>100):
    print("invalid score:")
elif(score>50 and score<90):
    print("Passable")
elif(score>90):
    print("Excelent")
elif(score<50):
    print("Bad")