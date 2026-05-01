print (" simple calculator")
a = int(input("first number : "))
b = int(input("second number : "))

c = input("operator : ")

if(c == "+"):
	print(a , "+", b,  "= ", a+b)
if(c== "×" or c== "*"):
	print (a , "×", b ,"= " ,a *b)
if(c== "-" ) :
	print (a, "-" , b, "=", a- b)
if (c=="÷" or c== "/"):
	print (a  ,"÷"  ,b ,"= " ,a / b)
