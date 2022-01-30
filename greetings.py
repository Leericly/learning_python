def greetings():
  def lotsaHello():
    maxHellos = int(input("How many hellos? "))
    currentHellos = 0
    while currentHellos < maxHellos:
      print("Hello")
      currentHellos += 1

  def lotsaGoodbye():
    maxGoodbyes = int(input("How many Goodbyes? "))
    currentGoodbyes = 0
    while currentGoodbyes < maxGoodbyes:
      print("Goodbye")
      currentGoodbyes += 1

  yourChoice = input("Hello or Goodbye? ")
  if yourChoice == "Hello" or "hello" or "h":
    lotsaHello()
    break
  if yourChoice == "Goodbye" or "goodbye" or "Good Bye" or "good bye" or "GB" or "gb" or "Gb" or "gB" or "G" or "g":
    lotsaGoodbye()
    break

greetings()
