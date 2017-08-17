import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t]) ##proper names for items like "c" "t"

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 2:
    return False
  list = sorted([(same(w, target), w) for w in list])
  list.reverse()
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

fname = input("Enter dictionary name: ").lower()
newFile = "newDic.txt"
exclude = input("enter any words you wish to exclude: ")
file = open(fname)
#newFile = open(newFile)
lines = file.readlines()
file.close()
file = open(newFile, 'w')
for line in lines:
    if line != exclude +"\n":
       file.write(line)

file = open(newFile)
lines = file.readlines()


while True:
  start = input("Enter start word:").lower()
  while not start.isalpha():
      start = input("Input error, please enter letters only:").lower()
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:").lower()
  while not target.isalpha():
      target = input("Input error, please enter letters only:").lower()
  break



count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

#github check

#josh's change