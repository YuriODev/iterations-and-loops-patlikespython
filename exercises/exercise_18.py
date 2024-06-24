# Your solution to Exercise 18
days=int(input("Enter a number of days:    "))
total_errors=0
for _ in range(days):
    errors=int(input("Enter number of errors:    "))
    total_errors+=errors
print(total_errors)