# Your solution to Exercise 11
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+= i/(i+1)
print(f"{sum:.2f}")
  