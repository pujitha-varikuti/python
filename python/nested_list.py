'''no=[1,10,15,[20,10,15],17,0]
print(len(no))
print(no[5])
print(no[3])
print(no[3][2])'''
#coding exerice matrix
'''list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
matrix=[[list1],[list2],[list3]]
print(f"{list1}\n{list2}\n{list3}")
row=int(input("enter the value: "))
column=int(input("enter the value :"))
matrix[row-1][column-1]='x'
print(matrix)'''
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
matrix=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
position=input("enter the value : ")
row=int(position[0])
column=int(position[1])
row_seleted=matrix[row-1]
row_seleted[column-1]='x'
print(f"{list1}\n{list2}\n{list3}")
'''list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]   #ikada fist manam final list oka index position tekunam taravatha a inside vuna list3 lo index position tesunam
final_list=[list1,list2,list3]
final_list[2][2]='x'
print(list1)
print(list2)
print(list3)'''