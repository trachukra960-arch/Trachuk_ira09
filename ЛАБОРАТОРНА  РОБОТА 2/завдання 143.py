n = intinput())
if n‹ 0 or n > 36:
    print ("The bet will not play!")
elif n == 0:
    print("Green")
elif 1 <= n <= 10 or 19 ‹= n ‹= 28:
    if n % 2 == 1:
      print("Red")
   else:
      print("Black")      
else:
    if n % 2 == 1:
      print( "Black")
   else:
      print("Red")
