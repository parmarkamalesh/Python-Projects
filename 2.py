# Write a program to check leap year
# what is a leap year: A Year having 366 days
# Non leap year: 365 days

# A year which is divisible by 4oo is a leap year. or a year divisible by 4 and a year divisible by 100 should not equal to zero.

x = int(input("Enter a year: "))
result = "Leap year" if x%400==0 else "Leap year" if x%4==0 and x%100!=0 else "Non leap year"
print(result)