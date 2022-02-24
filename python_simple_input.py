# This program takes a simple input from
# the console, stores it in a variable,
# and prints it back out.

my_input = input("Enter your name: ")
print(my_input)

# This code would allow simple text-
# based RPGs when combined with vari-
# ables.

# Ex.

print("Hello" + my_input "!")
print("Welcome to the dungeon!")

my_HP = 100

print("Your current HP is: " + my_HP)
print("You're in a dark cave.")
print("You hear something approach")
print("What do you do?")
print("")

my_action = input("(A)ttack, (R)un, (D)odge")

if my_action = "a" or "A":
    my_HP -= 10
    print("You were attacked by a bat!")
    print("You lost " + my_HP + "HP!")
else:
    print("You hear a noise but are ok.")
