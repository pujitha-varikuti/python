#in sets we cant change the values because that are immutable and duplicate values are not allowed and in sets their is no any specific oreder
'''set={1,56,54,85,21,0,1,"harika,"" hari",True,}
print(len(set))
print(set)
print(type(set))
set1={}
print(type(set1))
#set2=set()
#print(type(set2))
set.add(99)
print(set)
set.remove(1)
print(set)
set.discard(68)
print(set)
set.clear()
print(set)
print(set.pop())
print(set)'''
#set={1,4,5,8,(52,45,85),112}
#print(set)   # in sets we can add tuples not list 
#operations in sets 
#union
'''set1={12.51,'harika',51,'naveen'}
set2={85,51,45,62,'naveen'}
set3={45,97,0,10}
print(set1.union(set2,set3))
print(set1|set2|set3)
set1.update(set2)
set2.update(set3)
print(set1)
print(set2)
set1.update(['bhavani','satya'])
set1|=set2
print(set1)'''
#intersection
'''set1={'harika',78,90,87,889,'naveen'}
set2={'naveen','harika',67,80,889}
set3={78,85,90,67}
print(set1.intersection(set2))
print(set1 & set2)
print(set1.intersection_update(['harika'"satya"'bhavani']))
set1.intersection_update(set3)
print(set1)'''
#set methods like difference and difference update and symmertic difference and symmertic difference update
'''set1={'harika',78,90,87,889,'naveen'}
set2={'naveen','harika',67,80,889}
set3={78,85,90,67}
#print(set1.difference(set2))
#print(set1-set2)
#print(set1.difference_update((67,'hari')))
#print(set1.symmetric_difference(set2))#multiple sets cnat do this in method
#print(set1^set2^set3)#in this we can do multiple set methods
print(set1.symmetric_difference_update(('hari'"naveen")))'''
# disjoint checking in sets 
set1={'harika','sri''pujitha',34,67,78,78,787,99,556,23,"harikaa"}
set2={78,787,99,556,23,"harikaa"}
#print(set1.isdisjoint(set2))
#print(set2.issubset(set1))
#print(set1 <= set2)
#print(set1.issuperset(set2))
#print(set1>=set2)
#set1.clear()
#print(set1)
del set1
print(set1)