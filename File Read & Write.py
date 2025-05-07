# open file 
with open("dell.txt", "r") as file:
  content =file.read()
  print(content)

# write 
with open("output.txt", "w") as file:
  print(hel i am )


try:
    file = open("dell.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
   print("it doesn’t exist")
