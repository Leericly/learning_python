#Dictionary Play

mob_glossary_humanoid = {
    1:"Orc",
    2:"Goblin",
    3:"Moblin",
    4:"Ogre",
    5:"Giant"
}

mob_glossary_reptile = {
    1:"Snake",
    2:"Velociraptor",
    3:"Medusa"
}

mob_glossary_aquatic = {
    1:"Snapper",
    2:"Pirhana",
    3:"Shark",
    4:"Squid"
}

def printGlossary():
    choice1 = input("What directory do you want (1. Humanoid, 2. Reptile, 3. Aquatic): ")
    #Don't forget! Input is ALWAYS a String type. Either convert or deal with it!
    
    if choice1 == "1":
        print(mob_glossary_humanoid)
    elif choice1 == "2":
        print(mob_glossary_reptile)
    elif choice1 == "3":
        print(mob_glossary_aquatic)
    else:
        print("You did not make a proper choice!")

def listGlossaries():
    print(mob_glossary_humanoid)
    print(mob_glossary_reptile)
    print(mob_glossary_aquatic)

i = 0
while i < 3:
    printGlossary()
    i += 1

print("")
print("Let's make each dictionary contain 5 entries. Humanoid is okay, reptile has 3, aquatic has 4")
print("=" * 90)
print("")

mob_glossary_reptile[4] = input("Add one more reptile: ")
mob_glossary_reptile[5] = input("Add one more reptile: ")
print("")

mob_glossary_aquatic[5] = input("Add one more aquatic: ")
print("")
listGlossaries()
