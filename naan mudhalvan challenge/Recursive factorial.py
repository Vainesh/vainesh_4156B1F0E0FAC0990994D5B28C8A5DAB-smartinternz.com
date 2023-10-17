def rec_fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * rec_fact(n - 1)


number = int(input("enter the value:"))
result = rec_fact(number)
print("the factorial of{} is{}.".format(number, result))
