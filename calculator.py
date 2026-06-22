# Calculator by using IF-ELSE statement
num1 = int(input("Enter your num1 :"))
num2 = int(input("Enter your num2 :"))
opreator = input("Enter the opreation :")
add = num1+num2
Sub = num1-num2
mul = num1*num2
div = num1//num2
if opreator == "+" :
    print(add)
elif opreator == "-" :
    print (Sub)
elif opreator == "*":
    print(mul)
elif opreator == "//" :
    print(div)
else:
    print("not available opreator")