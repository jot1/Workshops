__author__ = 'jc450453'

sales = 0
while sales >= 0 :
    sales=float(input("Enter your sale :"))
    if (sales<1000 and sales>0):
      bonus=10/100*sales
      print ("your bonus is:",bonus)
    elif sales>=1000:
      bonus=15/100*sales
      print ("your bonus is:",bonus)

