# Basic Calculator

run = True

while run:
  try: # Attempting to handle errors of wrong type
    cmd = input("Which operator: ")
    a = int(input("Input for a: "))
    b = int(input("Input for b: "))
  except TypeError:
    print("Values are not the correct type!")

  print("Operator: ",cmd)
  print("a = ",a) #Discovered the ability to concatenate ints with a comma
  print("b = ",b)

  def mult(a, b):
    print("Result: ",a * b)

  def div(a, b):
    print("Result: ",a / b)

  def sub(a, b):
    print("Result: ",a - b)

  def add(a, b):
    print("Result: ",a + b)

  if cmd == "+":
    add(a, b)
  if cmd == "-":
    sub(a, b)
  if cmd == "*":
    mult(a, b)
  if cmd == "/":
    div(a, b)

  """
  choice = str(input("Press n to exit:"))
  if choice == "n":
    run = True
  else:
    run = False

  I couldn't get this part to run. As it stands, the program will keep looping until you manually exit.
