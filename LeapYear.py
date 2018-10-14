year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(" 1 {0} is a leap year".format(year))
       else:
           print("2 {0} is not a leap year".format(year))
   else:
       print("3 {0} is a leap year".format(year))
else:
   print("4 {0} is not a leap year".format(year))