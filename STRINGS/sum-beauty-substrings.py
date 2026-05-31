s = "aabcb"

# for i in range(len(s)):
#   for j in range(i, len(s)):
#     substrings = s[i:j+1]
#     # print(substrings)

#     freq = {}

#     for ch in substrings:
#       if ch in freq:
#         freq[ch] += 1
#       else:
#         freq[ch] = 1
    
#     beauty = max(freq.values()) - min(freq.values())
#     print(substrings, beauty)

total = 0
for i in range(len(s)):
  freq = {}
  for j in range(i, len(s)):
    ch = s[j]

    if ch in freq:
      freq[ch] += 1
    else:
      freq[ch] = 1

    beauty = max(freq.values()) - min(freq.values())
    total += beauty
print(total)
