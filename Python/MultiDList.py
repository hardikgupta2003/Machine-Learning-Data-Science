List1= [ [1, 2, 3, 5], [4, 6, 7, 9], [8, 10, 11, 13] ]
#Accesing the rows of the list
for i in List1:
  print(i, end = ' -- ')
  
#Accessing each element of a 2D-list 
print("\n")
for i in range(len(List1)):
  for j in range(len(List1[i])):
                 print(List1[i][j], end=" , ") 

print('\n')
List1 = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
List1.append([5, 10, 15, 20, 25]) 
print(List1)



matrix = [
    [1, 8 , 3],
    [7, 5, 6],
]
element = 5
position = [(i, row.index(element)) for i, row in enumerate(matrix) if element in row]
print(position)