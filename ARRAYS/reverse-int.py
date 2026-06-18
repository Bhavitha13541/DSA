# THIS IS ONLY FOR NATURAL NUMBERS

# I = 123
# I = 12345
I = -23458

rev = 0

# while I > 0:
#   digit = I % 10
#   rev = rev * 10 + digit
#   I = I // 10
# print(rev)

# 321
# 54321


negative = False

if I < 0:
  negative = True
  I = -I

rev = 0

while I > 0:
  digit = I % 10
  rev = rev * 10 + digit
  I = I // 10

if negative:
  rev = -rev

print(rev)

# -85432
