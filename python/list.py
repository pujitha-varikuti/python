'''A =[7,2,-7,88,'harika', True]
print(A)''' #brackets is very important and in list it will returan index error its means manam echina list length ki manam kavali ana posistion ki set avaledhu
# indaex position
roll_no=[1,3,89,64,76,28] #edhi front nudi count chesidhi
print(roll_no[1])
#back nudhin ietha index position andhi -1 ala evlai
roll_no=[1,3,89,64,76,28] 
print(roll_no[-1])
#list scling
roll_no=[1,3,89,64,76,28] 
print(roll_no[1:4])
#extend scling the value will be jump front to the next value
roll_no=[1,3,89,64,76,28] 
print(roll_no[0:2:4])
#sort values means it will directly  writen in ascending order
roll_no=[1,3,89,64,76,28] 
roll_no.sort()
print(roll_no)
#reverse the list inside elements
roll_no=[1,3,89,64,76,28] 
roll_no.reverse()
print(roll_no)
# we want to see max and min values
roll_no=[1,3,89,64,76,28] 
print(max(roll_no))
print(min(roll_no))
#append used to addd a value to the list only end and one value only
roll_no=[1,3,89,64,76,28] 
roll_no.append(49)
print(roll_no)
#we use extend add more values at end of the list
roll_no=[1,3,89,64,76,28] 
roll_no.extend([46,78,90])
print(roll_no)
# we use insert value to add a value in a particlar posistion
roll_no=[1,3,89,64,76,28] 
roll_no.insert(2,66)
print(roll_no)
#we want to replace the value use this
roll_no=[1,3,89,64,76,28] 
roll_no[2]=32
print(roll_no)
#do you wnant to change more values like this
roll_no=[1,3,89,64,76,28] 
roll_no[2:5]=32,78,32
print(roll_no)
#you want remove the values in a list it will remove only the first values
roll_no=[1,3,89,64,76,28] 
roll_no.remove(3) #ekada manam a value remove cheyalo rayali
print(roll_no)
# do you want remove the last elements we use the pop
roll_no=[1,3,89,64,76,28] 
print(roll_no.pop())
print(roll_no)
roll_no=[1,3,89,64,76,28] 
print(roll_no.pop(3))
print(roll_no)