#Set - is a collection of unique objects
sample_list = [1, 2, 3, 1, 1, 4, 2, 5]
print(type(sample_list))
print(sample_list)
print("\n")

sample_set = set(sample_list)
print(type(sample_set))
print(sample_set)
print("\n")

#Check if a number is present in a set
if 6 in sample_set:
  print("The number exists in the set")
else:
  print("The number does not exist in the set")

print("\n")

#Adding element to the set
mySet = set([])
mySet.add(100)
mySet.add(25)
mySet.add(50)
mySet.add(10)
mySet.add(30)
print(mySet)

#Remove an element from the set
mySet.remove(25)
print(mySet)

#remove will throw error, if the element is not present in the set
#mySet.remove(40)
#print(mySet)

#Discard will not throw error,even if the number does not exists in the set
mySet.discard(40)
print(mySet)

#Set Operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference

print("\n")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Set a : ", a)
print("Set b : ", b)

#Union means addition of sets
print("\n")
print("Union of two sets")
print(a.union(b))
print(a | b)

#Intersection means the common elements between two sets
print("\n")
print("Intersection of two sets")
print(a.intersection(b))
print(a & b)

#difference of A and B is the elements that exist in A but not in B
print("\n")
print("difference of A and B")
print(a.difference(b))
print(a - b)

#difference of B and A is the elements that exist in B but not in A
print("\n")
print("difference of B and A")
print(b.difference(a))
print(b - a)

#Symmetric difference is (union of sets - intersection of sets)
#removes common terms
print("\n")
print("Symmetric difference of a and b")
print(a.symmetric_difference(b))
print(a ^ b)
