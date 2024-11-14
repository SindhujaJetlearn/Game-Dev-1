#Tuples
studentDetails = ("Kim", 13, "Playing Badminton")
print(type(studentDetails))

#Packing - The process of assigning values to a tuple is known as packing.
address = (210, "Brickfeild Apartment", "Bangalore", "Karnataka", 564000)

#loop
for i in address:
  print(i)

#unpacking- Unpacking tuples assigns the objects in a tuple to multiple variables.
houseno, apartment, city, state, pin = address

print()
print("House number : ", houseno)
print("Apartment name : ", apartment)
print("City: ", city)
print("State : ", state)
print("Pin : ", pin)

#A tuple can be created without parentheses
print()
mypets = "dog", "cat", "parrot"
print(type(mypets))

#Nested tuple
myTuple = ("mouse", (1, 2, 3), [10, 45, 60])
#access tuple values using index
print(myTuple[0][3])

#To change the value of tuple
#tuple immutable- you cannot change value of tuple
#myTuple[0][3]="l"
#print(myTuple)

#Value of a list inside could be changed. because list is mutable
print(myTuple)
print(myTuple[2][2])
myTuple[2][2] = 100
print(myTuple)

#Concatenation
my_tuple1 = ("apple", "banana") 
my_tuple2 = ("cherry", "orange") 
my_tuple3 = my_tuple1 + my_tuple2 
print(my_tuple3)

#length
my_tuple = ("apple", "banana", "cherry") 
print(len(my_tuple))


#repeat
my_tuple = ("apple", "banana") 
print(my_tuple * 3)


#Slicing operator:
tuple1 = ('C', 'O', 'D', 'I', 'N', 'G')

print(tuple1[0:3])

print(tuple1[2:5])

#begin
print(tuple1[:4])

#end
print(tuple1[2:])

#Begin to end
print(tuple1[:])

#Negative index - last element index values is -1
print(tuple1[0:-3])

def find_vowels(input_string):
  vowels = ('a', 'e', 'i', 'o', 'u')
  found_vowels = []

  for char in input_string.lower():
      if char in vowels:
          found_vowels.append(char)

  return tuple(found_vowels)

text =input("Enter the text : ")

result = find_vowels(text)

print("Vowels found:", result)

print("\n----------------------------------")
print("Sets")

#Sets-collection of unique elements
list1 = [1, 2, 3, 4, 5, 1, 2, 4, 4, 5]

#Convert list to set
set1 = set(list1)
print(type(set1))
print(set1)

#check if an element exists in the set
if 6 in set1:
  print("Yes the value exists in the set")
else:
  print("No, the value does not exist in the set")

#create and add values to set
myset = set([])
myset.add(20)
myset.add(30)
myset.add(70)
myset.add(100)
myset.add(80)
print(myset)

#Remove values from set
myset.remove(100)
print(myset)
#Remove throws error, if the value doesnt exists in set
#myset.remove(5)
#print(myset)

#Discard does not throw error, even if we dont have the value in the set
myset.discard(5)
print(myset)

print()
print("Set Operations ")
#1.Union
#2.Intersection
#3.Difference
#4.Symmetric difference

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("a :", a)
print("b :", b)

#1.Union - adding two sets
print()
print("Union of two sets ")
print(a.union(b))
print(a | b)

#2.Intersection - common element between the sets
print()
print("Intersection of two sets")
print(a.intersection(b))
print(a & b)

#3.Difference of A and B - element in A but not in B
print()
print("Difference of set a and b ")
print(a.difference(b))
print(a - b)

#Difference of B and A - element in B but not in A
print()
print("Difference of set b and a ")
print(b.difference(a))
print(b - a)

#4.Symmetric difference - (union-intersection of set)
#removes the common from the given sets
print()
print("Symmetric difference")
print(a.symmetric_difference(b))
print(a ^ b)