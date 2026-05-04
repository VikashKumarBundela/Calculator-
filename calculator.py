print (" simple calculator")
a = float(input("first number : "))
b = float(input("second number : "))

c = input("operator (+, - , * , / ) : ")

if(c == "+"):
	print(a , "+", b,  "= ", a+b)
if(c== "×" or c== "*"):
	print (a , "×", b ,"= " ,a *b)
if(c== "-" ) :
	print (a, "-" , b, "=", a- b)
if(c=="÷" or c== "/"):
     if (b== 0):
	       print(" Result : Undefined ")
     else:
           print (a  ,"÷"  ,b ,"= " ,a / b)
else:
	print( " invalid operator ")
	
	
