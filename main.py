name = input("Input a name")
age = input("How old are you")
try:
  age = int(age)
  print(f"{name}, {age} years old")
except:
  print("Enter a whole number as your age mate.")
