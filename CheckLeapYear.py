year = int(input("Enter the year: "))

if year%400 == 0 | (year%4 == 0 & year%400 != 0):
    print("This year ",year," is a leap year")
else:
    print("This is not leap year")