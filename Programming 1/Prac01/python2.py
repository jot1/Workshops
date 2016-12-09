firstName = 'Prabhjot'
lastName='Kaur'
age=25
fruits=["orange","pineapple","banana","mango"]

sequence=[1,2,3,4,5,6,7,8,9]
print('Today is the first day of programming class')
print(firstName)
print(firstName,lastName)
print(firstName+ " " +lastName)
print(age)
print(firstName+ " " +lastName +" "+ "25")
print(firstName+ " " +lastName ,"25")
print(fruits)
print(fruits[0])
"for loop"

for value in fruits:
    print(value)
for value in sequence:
    print(value)

    "while loop"
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