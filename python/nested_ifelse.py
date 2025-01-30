#nested if
'''number = int(input("enter the number :"))
if number>=50:
     print("you are ready")
     age=int(input("enter the age :"))
     if (age<=60):
          print("your are not ready")
else:
     print("you should take the worng input from the user")  '''    

#nested_if else
'''
number = int(input("enter the number :"))
if number>=50:
     print("you are ready")
     age=int(input("enter the age :"))
     if (age<=60):
          print("your are not ready")
     else:
         print("your are greater than 60")      
else:
     print("i am tried")'''
#nested elif(else if) we can you two are more condithion 
'''number = int(input("enter the number :"))
if number>=50:
     print("you are ready")
     age=int(input("enter the age :"))
     if (age<=60):
          print("your are not ready")
     elif(age>60): 
           print("you are ready") 
     else:
         print("your are greater than 60")      
else:
     print("i am tried")'''

 #exerice on elif
'''weight=int(input("enter the weight in kgs : "))    
height=float(input("enter the height in meters :"))
BMI=round(weight/height**2)
if BMI<35:
     print(f"your weight{BMI} is so less you are weak")
elif BMI>40:
     print(f"your weight {BMI} is not great you need take healthy food")   
elif BMI>40:
     print(f"you weight {BMI} is ok but you take care of that")       
elif BMI>50:
     print(f"your weight{BMI} is great crry like that good")
else:
     print("you take care of your own self bye")'''
# exerice leap year
'''year=int((input("enter the number : ")))
if year%4==0:
     print("its a leap year")     
else:
     print("it's not a leap year")    ''' 

# exerice for pizza order
'''size= input("what size of pizza do you want(s/m/l)? ")
bill=0
if size== 's':
    bill+=100
elif size=='m':
    bill+=200
else:
    bill==300
do_you_want=input("pepperion for small pizza(y/n):") 
if do_you_want=='y':
    bill+=30  
else:
    bill+=50
DO_YOU_WANT=input("extra cheese  for any size pizza(y/n):")    
if DO_YOU_WANT=='y':
    bill+=20
else:
    print("wrong input ")  
print(f"your total bill:{bill}") '''