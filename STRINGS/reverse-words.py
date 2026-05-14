def reverse_words(s):
  words = s.split()
  print(words)
  # ['All', 'The', 'Best']
  rev = words[: : -1]
  print(rev)
  # ['Best', 'The', 'All']
  res = " ".join(rev)
  return res
print(reverse_words("All The Best"))

# Best The All
  
