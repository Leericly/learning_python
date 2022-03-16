myFactor = int(input("Get the factorial of what number: "))

def factorial(n, depth):
    if (depth < 7):
        if (n > 1):
            return n*factorial(n-1, depth + 1)
        else:
            return n
    else:
        print("ERROR: Maximum recursion depth exceeded.")
        return 0

print("Your factorial is: ", factorial(myFactor, 0))
