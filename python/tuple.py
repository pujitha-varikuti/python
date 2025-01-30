#the difference b/w lust and tuple is first it is denoted by round brackts and in tuples we cant change the valuses once the tuple created
tuple=(10,34,67,89,-90,'harika',True)
tuple1=(89,76,12,54,45,78,54,85,45)
tuple3=tuple+tuple1
print(tuple)
print(type(tuple))
print(len(tuple))
print(tuple[1])
print(tuple[-1])
print(tuple1[0:5])
print(tuple[0::5])
print(tuple3)
print(len(tuple3))
print(tuple3[2])
print(tuple1.count(54))
print(tuple1.index(54))
list=[1,45,85,-25,67]
print(tuple(list))