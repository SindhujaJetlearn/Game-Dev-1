name=input("Enter your name : ")
print(name)

student = {
  "name": "Paolo", 
  "age": 12, 
  "hobby": "Playing games"
}

#Accessing the values of a dictionary - using keys
print(student["name"])
print(student["age"])

#Access list of all keys
print(student.keys())

#Access list of all values
print(student.values())

#loop
print()
for i in student.keys():
  print(i, ":", student[i])

#Check if a key exists in the dictionary or not
print()
if "marks" in student:
  print("Key exists")
else:
  print("Key does not exist")

#Add a new key-value pair to the dictionary
print()
student["favSubject"] = "English"
print(student)

#Delete a key-value pair
print()
del (student["hobby"])
print(student)

#Change a value in the dictionary
print()
subject = input("What is your fav subject ? ")
student["fav subject"] = subject
print(student)

#Store a list inside a dictionary
print()
student["marks"] = [98, 67, 90, 94, 100]
print(student)

#Acces a value in list stored inside a dictionary
print(student["marks"][4])
print(student["marks"][2])

#Nested Dictionary
classroom = {
  "Remi": {
    "age": 12,
    "hobby": "Dancing"
  },
  "Olivia": {
    "age": 11,
    "hobby": "Singing"
  }
}
print()
print(classroom.keys())
print(classroom.values())

#Access value of nested dictionary
print(classroom["Olivia"]["hobby"])

#loop
print()
for i in classroom.keys():
  print(i, ":", classroom[i])

#create an empty dictionary
countryDb = {}
#infinite loop
while True:
  #print menu
  print("1. Insert")
  print("2. Display all countries")
  print("3. Display all capitals")
  print("4. Get capital")
  print("5. Delete")
  #get user choice
  choice = int(input("Enter your choice(1-5)"))
  #if insert
  if choice == 1:
    country = input("Enter country :").upper()
    capital = input("Enter capital :").upper()
    countryDb[country] = capital
  #to display all countries
  elif choice == 2:
    print(list(countryDb.keys()))
  #to display all capitals
  elif choice == 3:
    print(list(countryDb.values()))
  #to display capital of a specific country
  elif choice == 4:
    country = input("Enter country").upper()
    #print(countryDb[country])
    print(countryDb.get(country))
  #to delete entry of a specific country
  elif choice == 5:
    country = input("Enter country :").upper()
    del countryDb[country]
  #if none of the above option
  else:
    break

#Write a python program that uses a dictionary that contains ten usernames and passwords. The program should ask the user to enter their username and password. If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. If the password is correct, then the program should tell the user that they are now logged in to the system. 

users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}


# Prompt user for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username exists
if username not in users:
    print("Invalid user. You are not a valid user of the system.")
else:
    # Check if the password is correct
    if users[username] == password:
        print("You are now logged in to the system.")
    else:
        print("Invalid password. Please try again.")