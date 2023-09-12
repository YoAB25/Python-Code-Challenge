# Project Day 3 : Treasure Island (Beginner)
#
print("==========================\n")
print("Welcome to Treasure Island\n")
print("Your mission is to find the treasure\n")
#
inp1 = str(input("Which direction do you want left or right ? ")).lower()
if (inp1=="right"):
    print(" You go in a cave and you've found a bear")
elif (inp1 == "left"):
    inp2 = str(input("Good choice now you're next to a river! What do you choose now?")).lower()
    if (inp2 == "swim"):
        print("Game Over! You are eaten by a crocodile")
    elif(inp2 == "wait"):
        inp3 = str(input("Hmmm! still going! Now you've to choice which door you want to go through ?")).lower()
        if(inp3=="blue" or inp3=="red"):
            print("Game Over ! It's a fire out there")
        elif(inp3=="yellow"):
            print("Well done! You are so clever!")
        else:
            print("Good try! But the game is over because of hack attempting")

    else:
        print("Good try! But the game is over because of hack attempting")
else:
    print("Good try! But the game is over because of hack attempting")

