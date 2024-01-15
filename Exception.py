

try :
  num = int(input("input a number"))
except ValueError:
  print("Is wrong zNumver")
  num=7
  print(f"you enter number{num}")