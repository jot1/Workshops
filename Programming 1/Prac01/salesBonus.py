__author__ = 'jc450453'
choice = input(">>> ").upper()
while choice != "Q":
 if choice == "C":
  sales=float(input("Enter your sale"))
while sales>=0:
 print("Enter your sale:")
if sales<1000:
  bonus=10/100*sales
  print ("your bonus is:",bonus)
elif sales>=1000:
  bonus=15/100*sales
  print ("your bonus is:",bonus)
else:
  print("Invalid option")
choice = input(">>> ").upper()
print("Thank you.")

