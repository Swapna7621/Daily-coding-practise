n = int(input("Enter a number of term: "))
a = 0
b = 1
print("Fibonaccis series:")
for i in range(n):
  print(a, end=" ")
  c = a+b
  a = b
  b = c
