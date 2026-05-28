# s = "tree"
# d = {}
# for i in range(len(s)):
#   ch = s[i]

#   if ch in d:
#     d[ch] += 1
#   else:
#     d[ch] = 1

# print(d)
# res3 = ''
# print(sorted(d.items()))
# res1 = sorted(d.items())
# for j in range(len(d)):
#   res2 = (res1[j][0] * res1[j][1])
#   res3 += res2
# print(res3)


def sort_character_frequency(s):
  d = {}
  for i in range(len(s)):
    ch = s[i]
    if ch in d:
      d[ch] += 1
    else:
      d[ch] = 1
  res1 = sorted(d.items(), key = lambda x : x[1], reverse=True)
  res3 = ''
  for j in range(len(d)):
    res2 = (res1[j][0] * res1[j][1])
    res3 += res2
  return res3
print(sort_character_frequency("aaaccc"))

# aaaccc


