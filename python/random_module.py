'''import random
a = random.randint(0,1)
print(a)
if a==0:
    print("the coin is tail")
else:
    print("the coin is head")    '''
# exerice for who pay the bill we use split function
import random
names=(input("enter the names separated by comma :"))
split=names.split(",")
print(split)
length=len(split)
after_split=(random.randint(0,length-1))
print(f"{split[after_split]}will pay the bill")
#print(after_split)
# we can also use the choice function
names=(input("enter the names separated by comma :"))
split=names.split(",")
print(split)
print(random.choice(split)+" will pay the bill")