s = "pqpqs"
k = 2

count = 0

for i in range(len(s)):
  for j in range(i,len(s)):
    subs = s[i:j+1]


    if len(set(subs)) == k:
      count += 1


print(count)











