day = 13
month = "March"
year = 2022

temp = 64

#The code below lists out info about a variable.

print("The variable 'day' is a: ")
print(type(day))
print(f"and it's value is: {day}")

print("The variable 'temp' is a: ")
print(type(temp))
print(f"and it's value is: {temp}")

#Since it's been used twice, I made a function to
#perform the activity.

def listVariable(a):
  print("The variable is a: ")
  print(type(a))
  print(f"and it's value is: {a}")

listVariable(day)
listVariable(month)
listVariable(year)
listVariable(temp)

#I discovered that Python won't get the name of a
#variable as a string for use in printing in the
#console. So I'm going to ask the user for input
#so the user knows what is being entered for the
#variable info to be returned.

dayChoice = input("What's numbered day is it: ")
listVariable(day)
                  
monthChoice = input("What's umbered month is it: ")
listVariable(month)
                    
yearChoice = input("What year is it: ")
listVariable(year)
                    
tempChoice = input("What is the temp: ")
listVariable(temp)                    
