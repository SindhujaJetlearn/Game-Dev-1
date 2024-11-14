# Count the occurrence of vowels in the string entered by the user

# Approach - 1
inputStr = input("Enter the string - ")
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for c in inputStr:
  if c in vowels:
    vowels[c] += 1

print(vowels)

# Approach - 2
inputStr = input("Enter the string - ")
vowelsList = ['a', 'e', 'i', 'o', 'u']
vowels = {}

for c in inputStr:
  if c in vowelsList:
    if c in vowels:
      vowels[c] += 1
    else:
      vowels[c] = 1

print(vowels)

# Find if the number entered by the user is a Panagram or not - A pangram is a sentence containing every letter in the English Alphabet.

numberAsString = input("Enter the number - ")

numCount = {
  "1": 0,
  "2": 0,
  "3": 0,
  "4": 0,
  "5": 0,
  "6": 0,
  "7": 0,
  "8": 0,
  "9": 0,
  "9": 0
}

for num in numberAsString:
  if num in numCount:
    numCount[num] += 1

panagram = True
for count in numCount.values():
  if count == 0:
    panagram = False

if panagram:
  print("Entered number is a Panagram")
else:
  print("Entered number is not a Panagram")

# Python3 program to
# Check if the string is pangram
import string
def ispangram(str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for char in alphabet:
    if char not in str.lower():
      return False

  return True

# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if (ispangram(string) == True):
  print("Yes, its a Panagram")
else:
  print("No, its not a Panagram")


  
  
