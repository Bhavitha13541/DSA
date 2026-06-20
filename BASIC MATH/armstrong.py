num = 153
n = len(str(num))
original = num
sum = 0


while num > 0:
  digit = num % 10
  
  sum += digit ** n
  num = num // 10
if sum == original:
  print(True)
else:
  print(False)