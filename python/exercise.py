'''weight= (input("Enter the weight: "))
height= (input("Enter the height: "))
bmi=int(weight)/float(height)**2

print(int(bmi))'''
#round function
'''print(round(5))
print(round(5.665466,2))
print(round(7.5))
print(round(6.5))
print(round(674,2))
print(round(674,-1))
print(round(11.5))
print(round(12.5))
print(round(675,-1))
print(round(1212,-2))
print(round(477.87353,-2))
print(type(round))'''
 # f string
'''name = 'harika varikuti'
age = 21
height = 4.4
father_age = 60
print("my name is "+name,"my age is"+str(age), "my height is "+str(height) ,"meters")
print("my name is",name, "my age is",age, "my height is ",height,"meters")
print(f"my name is {name} my height is {height} my age is{21} meters")
print(f"harika father age is {age*3} years")
print(f"harika brother age {age+6} years")
print (f"harika mother age is {age*2} yeras old")
print(f"my age{father_age-35} yeras old")'''
# exerice like count you age 
'''age = int(input("enter the present age : "))
years_left = 90-age
days_left=years_left*365
months_left=years_left*12
weeks_left = years_left*52
print(f"you have {years_left} years and {days_left}  days and {months_left}  months and {weeks_left}  weeks to levae")
age = input("enter the age ; ")
left_age=90-int(age)
print(f"youn have{left_age*365} days {left_age*12} months {left_age*52} weeks {left_age} years")
age_1=int(input("enter the current age : "))
age_2 =int(input("enter the expetation age : "))
print(f"you have {age_1*365-age_2*365}  days and{age_1*12-age_2*12} months and {age_1*52-age_2*52} weeks and {age_1-age_2} years")'''
'''age = 22
left_age = 100
print(f" you have {left_age-age} years and {left_age*365-age*365} days and {left_age*12-age*12} months and {left_age*52-age*52} weeks ")'''
# just an doubt you eant know how many letter in youe name
'''name="harika"
print(len(name))
name="harika"
print(name[0])
name="harika"
print(name[0:4])
name="harika"
print(name.count('i'))
name="HARIKA"
print(name.lower())'''
#love calculator
name_1=input("enter your name : ")
name_2=input("enter your name : ")
name=(name_1+name_2)
hari=(name.lower())
t=hari.count('t')
r=hari.count('r')
u=hari.count("u")
e=hari.count('e')
true=t+r+u+e
l=hari.count('l')
o=hari.count('o')
v=hari.count('v')
e=hari.count('e')
love=l+o+v+e
true_love=int(true+love)
print(true_love)
if true_love>50 or true_love>90:
 print(f"your{true_love} is greater so you can love") 
 if true_love<=40 and true_love>=90:
  print(f"yoer{true_love} is nice you can love each other")
else:
 print(f"your love is {true_love} not much grater so please stop")  