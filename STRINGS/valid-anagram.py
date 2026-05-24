            #  SOLUTION 1
from itertools import permutations
word = "abc"
target = "bca"
anagrams = []
for p in permutations(word):
  anagram =  ''.join(p)
  anagrams.append(anagram)

if target in anagrams:
  print(True)
else: 
  print(False)


  # SOLUTION 2


if sorted(word) == sorted(target):
  print(True)
else:
  print(False)
  

    
  

