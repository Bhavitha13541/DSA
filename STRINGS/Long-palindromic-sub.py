
# s = "a"
# subst = []
# palin = []
# for i in range(len(s)):
#   for j in range(i, len(s)):
#     sub = s[i:j+1]
#     subst.append(sub)
# print(subst)

# for ch in subst:
#   if ch == ch[::-1]:
#     palin.append(ch)
# print(palin)

# longest = ""

# for k in palin:
#   if len(k) > len(longest):
#     longest = k

# print(longest)

                                    #  LITTLE OPTIMIZATION 


s = "pqrpq"

longest = ""

for i in range(len(s)):
  for j in range(i, len(s)):
    sub = s[i:j+1]

    if sub == sub[::-1] and len(sub) > len(longest):
      longest = sub

print(longest)






