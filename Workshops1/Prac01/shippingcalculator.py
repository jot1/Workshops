__author__ = 'jc450453'

NumberofItem=1
while NumberofItem>0:
  NumberofItem=int(input("Enter Number of Items :"))
  Costperitem=float(input("Enter your cost per item :$"))

  Totalshipcost=NumberofItem*Costperitem;
  if(Totalshipcost>100):
        Totalshipcost=Totalshipcost - (10/100*Totalshipcost)
        print("the total cost for deliver your product is: " ,Totalshipcost)



