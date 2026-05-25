s = "abcde"
goal = "cdeab"


          # BRUTEFORCE APPROACH

# for i in range(len(s)):
#   shift = s[i:] + s[:i]
#   if shift == goal:
#     print(True)

        # OPTIMAL APPROACH

if len(s) != len(goal):
  print(False)
elif goal in (s + s):
  print(True)

# True

# if --> if condition works when conditon is true and return or prints true value, if condition is false it goes for elif or else conditions.

# elif --> elif condition works if, if condition is not true 