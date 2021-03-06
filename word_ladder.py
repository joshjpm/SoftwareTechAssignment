# Module re provides string searching as well as support regular expressions
import re

# Returns how many characters match the end target word.
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

# Creates a list of words
def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]
# Finds possible paths
def find(word, words, seen, target, path):
  list = []

  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)

# If there is no matching words then there is no possible path
  if len(list) == 2:
    return False
  list = sorted([(same(w, target), w) for w in list])
  list.reverse()
# If it is not the same as well as there is one word
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
# Add this word to the path
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

# Prompts the user to input the name of their dictionary file.
# Then prompts the user if they would like to exclude any words.
fname = input("Enter dictionary name: ").lower()
newFile = "newDic.txt"
exclude = input("Enter any words you wish to exclude from the path: ")
file = open(fname)

#newFile = open(newFile)
lines = file.readlines()
file.close()
file = open(newFile, 'w')
for line in lines:
    if line != exclude +"\n":
       file.write(line)

# Opens the file.
file = open(newFile)
lines = file.readlines()

# Prompts the user enter a starting word
while True:
  start = input("Enter start word:").lower()
  while not start.isalpha():

# If the user does not enter a lower case string then an error is displayed
# and they are once again prompted to enter a valid input.
      start = input("Input error, please enter letters only:").lower()
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)

# Prompts the user enter a target word
  target = input("Enter target word:").lower()
  while not target.isalpha():

# Same as the start word, if the user does not enter a valid input
# then a error is returned.
      target = input("Input error, please enter letters only:").lower()
  break



count = 0
path = [start]
seen = {start : True}

# Prints the path found by the program
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)

# If no path is found then it is printed to the user.
else:
  print("No path found")
