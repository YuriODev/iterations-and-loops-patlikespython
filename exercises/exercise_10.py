# Your solution to Exercise 10
pounds=int(input("Enter pounds:   "))
kilograms=0
for i in range(1,pounds+1):
  kilograms+=0.453
  print(f"{i} {kilograms:.2f}")
