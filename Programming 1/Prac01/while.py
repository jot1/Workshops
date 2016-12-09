__author__ = 'jc450453'

 number=0
    while(number<10):
        print(number)
        number=number+1
age=int(input("Enter your age: "))
if(age < 18):
    print("you are too young")
elif (18<=age and age< 50):
    print('you are major')
else:
   print ('you are too old')
