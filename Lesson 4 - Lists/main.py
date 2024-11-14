#Create 1D list
a = [34, "hi", True, 23.4, 7]
print(a)

#Index - access list values - starts with 0
print(a[1])
print(a[-1])

#len - number of elements in the list
print(len(a))

#Add values to list - last 
a.append("Rock")
print(a)

#Add values to list - at a particular index 
a.insert(3,"hello")
print(a)

#Remove last value from list
a.pop()
print(a)

a.pop(3)
print(a)

#Create 2D list
print()
print("2D list ")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

#number of rows
print("Number of rows   : ", len(matrix))

#number of columns
print("Number of columns: ", len(matrix[0]))

#Access the values of 2D list
print(matrix[1][1])
print(matrix[0][2])
print(matrix[-1][-1])

#Loop through 2D list
for i in range(3):
  for j in range(3):
    print(matrix[i][j], end=" ")
  print("\n")

print()
#Take input from user to create 2D list
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))

matrix1 = []  #hold all the values
for i in range(rows):
  temp = []  #hold elements in row wise
  for j in range(columns):
    x = int(input("Enter the element : "))
    temp.append(x)
  matrix1.append(temp)

for i in range(rows):
  for j in range(columns):
    print(matrix1[i][j], end=" ")
  print("\n")

# Take the square-matrix as input and print the diagonal elements
print("\n")
n = int(input("Enter the dimensions of the matrix - "))
matrix2 = []
for i in range(n):
  temp = []
  for j in range(n):
    x = int(input("Enter your element - "))
    temp.append(x)
  matrix2.append(temp)

for i in range(n):
  print(matrix2[i][i])

#Addition of 2 matrix
print("\nAddtion of 2 matrix")

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [8, 9]]
result = [[0, 0], [0, 0]]

for i in range(0, 2):
  for j in range(0, 2):
    result[i][j] = matrixA[i][j] + matrixB[i][j]

#Print the result
for i in range(0, 2):
  for j in range(0, 2):
    print(result[i][j], end=" ")
  print("\n")

