n = 121

if n < 0:
  print("false")

original = n
rev = 0
while n > 0:
  digit = n % 10
  rev = rev * 10 + digit
  n = n // 10

if rev == original:
  print("true")