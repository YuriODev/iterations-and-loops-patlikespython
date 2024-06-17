# Your solution to Exercise 8
n=int(input("Enter number:    "))
for i in range(2, n+1):
    if i % 2 == 1:
        continue

    if i == n - 1 or i == n:
        print(i)
    else:
        print(i, end=" ")