import rentCostume
import returnCostume

def welcome():
    print("-------------------------------------------------------")
    print()
    print("         Welcome to costume rental application")
    print("             Designed by Himanshu Yadav :) ")
    print()
    print("-------------------------------------------------------")


def displayingMessage():
    
    """An introductory screen will appear upon launching the program."""

    while True: 
        print("\n")
        print("Select a desirable option")
        print("(1) || Press 1 to rent a costume.")
        print("(2) || Press 2 to return a costume.")
        print("(3) || Press 3 to exit.")
        selectedOption = input("Enter a option: ")
        if selectedOption == "1":
            print("\n")
            print("Let's rent a costume :)")
            print("\n")
            rentCostume.rentCostume()

        elif selectedOption == "2":
            print("\n")
            print("Let's return a costume :)")
            print("\n")
            returnCostume.returnCostume()

        elif selectedOption == "3":
            print("\n")
            print("         Greetings and thank you for visiting our store :)")
            exit()

        else:
            print("\n")
            print("Invalid input! :( ")
            print()
            print("Please select the value as per the provided options :)")

welcome()
displayingMessage()
