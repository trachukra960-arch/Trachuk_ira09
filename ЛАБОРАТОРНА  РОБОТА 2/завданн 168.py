n = int (input))
a = n // 100
b = n // 10 % 10
c = n % 10
if a +c>b:
      print(">")
elif a + c < b:
      print("‹")
else:
      print("=")
