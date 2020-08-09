
girlandboy=int(input("Click 1 if your kid is a girl click 2 if male:"))

if girlandboy == 1: 
     dadhei=int(input("Your father's height:"))
     momhei=int(input("Your mother's height"))
     print("Your child's height:",((dadhei-13)+momhei)/2)

elif girlandboy==2:
     dadhei=int(input("Your father's height:"))
     momhei=int(input("Your mother's height"))
     print("Your child's height:",(dadhei+(momhei+13))/2)
else:
 print("You entered the wrong value You have to enter 1 or 2")