import datetime
import random

def getFileContent():
    
    """Here, we are extracting data from the txt file as a list."""
    
    file = open("costumes.txt","r")
    data = file.readlines()
    file.close()
    return data


def getDictionary(fileContent):

    """Here, we are arranging the data from which is in list to Dictionary."""
    
    data = {}
    for index in range(len(fileContent)):
        data[index+1] = fileContent[index].replace("\n","").split(",")
    return data


def printCostumes(mainData):
    
    """Here, we create a table which enhances the user experince."""
    
    print("-----------------------------------------------------------------------------------")
    print("S.No.", "\t", "Costume Name", "\t\t", "Brand", "\t\t\t", "Price", "\t\t", "Quantity")
    print("-----------------------------------------------------------------------------------")
    for key,value in mainData.items():
        print(str(key)+str("."), "\t", value[0], "\t\t", value[1], "\t\t", value[2], "\t\t", value[3])
    print("-----------------------------------------------------------------------------------")            
    return ""

def getValidSno(mainData):

    """we are validating the serial number."""

    validSno = False
    while validSno == False:
        SNo = input("Enter Serial Number: ")
        try:
            if SNo.isdigit():
                SNo = int(SNo)
                if SNo > 0 and SNo <= len(mainData):           
                    if int(mainData[SNo][3]) == 0:   
                        print()
                        print("Costume is out of stock!")
                        print()
                        print("Try another!")
                        print()
                        print(printCostumes(mainData))
                        continue
                    else:
                        validSno = True
                        print(f"The serial number of the costume is {SNo}.")
                        print()
                        print("-------------------------------------------")
                        print("       The costume is available.           ")

                        print("-------------------------------------------")
                        print("\n")
                    return SNo
                else:
                    print("Your number is out of the options provided.")
                    print("\n")
            else:
                print("Please type a number next time.")
                print("\n")
        except:
            print("Invalid Serial Number!")

def getValidQuantity(mainData,SNo):

    """we are validating the quantity of costume to be rented."""

    cart = []
    tempRentBill = []
    validQuantity = False

    while validQuantity == False:
        quantity = input("Enter the total number of dresses you want to rent: ")
        try:
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= int(mainData[SNo][3]):
                    validQuantity = True
                    mainData[SNo][3] = str(int(mainData[SNo][3]) - quantity)
                    return quantity
                else:
                    print("Quantity provided is greater than we have in stock.")
                    print("So, Please enter the quantity which doesn't goes exceeding our stocks.")
                    print("\n")
            else:
                print("Please type a number next time.")
                print("\n")
        except:
            print("Invalid Quantity!")
            
def rentCostume():

    """This function is executed when the user wants to rent the costumes."""

    userWantsClothes = True
    cart = []
    tempRentBill = []
    
    while userWantsClothes == True:
        print(printCostumes(mainData))
        SNo = getValidSno(mainData)
        quantity = getValidQuantity(mainData,SNo)
        
        flag = True
        for costume in cart:
            if costume[0] == SNo:
                costume[1] += quantity
                flag = False
        if flag:
            cart.append([mainData[SNo][0], quantity])
            tempRentBill.append([mainData[SNo][0], mainData[SNo][1], mainData[SNo][2], quantity])

        valid_input = False
        while valid_input == False:
            wantAnother = input("Wanna rent more(yes/no)? ")
            if wantAnother.lower() == "yes":
                print("\n")        
                print(f"Your Cart: {cart}")
                print("\n")
                valid_input = True
                break
            elif wantAnother.lower() == "no":
                print("\n")
                generateBill(tempRentBill)
                userWantsClothes = False
                valid_input = True
            else:
                print("Invalid Input !!")
                print("\n")
                continue 
        updateTextFile(mainData)
        print("\n")


def generateBill(tempRentBill):
    """In this function we are passing 2d list"""
    
    validName = False
    while validName == False:
        Name = str(input("Enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
            
    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        
    
    Address = str(input("Enter your address: "))
    GST = random.randint(1000, 5000)
    Year = (datetime.datetime.now().year)
    Month = (datetime.datetime.now().month)
    Day = (datetime.datetime.now().day)
    Hour = (datetime.datetime.now().hour)
    Minute = (datetime.datetime.now().minute)
    Second = (datetime.datetime.now().second)
    microSecond = (datetime.datetime.now().microsecond)
    print("\n")
    print("------------------------------------------Costume Rental Shop--------------------------------------------")
    print("                                           Kathmandu, Nepal                                              ")
    print(f"                                             GST.NO:-{GST}                                              ")
    print("-----------------------------------------------Rent Bill----------------------------------------------------")
    print(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    print(f"Customer Name: {Name}")
    print(f"Phone Number: {phoneNumber}")
    print("---------------------------------------------------------------------------------------------------------")
    print("S.No.", "\t", "Costume Name", "\t\t", "Brand", "\t\t\t", "Rate", "\t\t", "Quantity", "\t\t", "Amount")
    print("---------------------------------------------------------------------------------------------------------")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempRentBill)):
        counter += 1
        for j in range(len(tempRentBill[i])):
            dollarprice = float(tempRentBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempRentBill[i][3]
            row = row + str(tempRentBill[i][j]) + "\t\t"    
        print(counter,"\t",row, "\t", priceDetail)
        finalPrice = finalPrice + priceDetail
        row = ""
            
    print("---------------------------------------------------------------------------------------------------------")
    print(f"                                         Total Price: ${finalPrice}                                       ")
    print("---------------------------------------------------------------------------------------------------------")
    print("                                    Thank you for vising our store                                       ")
    print("                                           Visit again :)                                                ")
    print()
    print("-------------------------------Bill has also been generated in txt file.---------------------------------")

 
    #This code prints the bill in txt formate.
    text = f"Rent-{Name}.txt"
    file = open(text,"w")
    file.write("------------------------------------------Costume Rental Shop--------------------------------------------")
    file.write("\n")
    file.write("                                           Kathmandu, Nepal                                              ")
    file.write("\n")
    file.write(f"                                             GST.NO:-{GST}                                              ")
    file.write("\n")
    file.write("----------------------------------------------Rent Bill--------------------------------------------------")
    file.write("\n")
    file.write(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    file.write("\n")
    file.write(f"Customer Name: {Name}")
    file.write("\n")
    file.write(f"Phone Number: {phoneNumber}")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("S.No. \t Costume Name \t\t Brand \t\t\t price \t\t Quantity \t\t Amount")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(tempRentBill)):
        counter += 1
        for j in range(len(tempRentBill[i])):
            dollarprice = float(tempRentBill[i][2].replace("$",""))
            priceDetail = dollarprice * tempRentBill[i][3]
            row = row + str(tempRentBill[i][j]) + "\t\t\t"   
        file.write(f"{counter} \t\t {row} \t\t{priceDetail}")
        file.write("\n")
        finalPrice = finalPrice + priceDetail
        row = ""
            
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"                                    Total Price: ${finalPrice}                                          ")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("                                   Thank you for vising our store                                        ")
    file.write("\n")
    file.write("                                           Visit again :)                                                ")
    file.close()
    
    
      
def updateTextFile(mainData):

    """Here, we are inserting the updated data to the txt file in string data type."""
    
    file = open("costumes.txt", "w")
    for value in mainData.values():
        file.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n")
    file.close()

fileContent = getFileContent()
mainData = getDictionary(fileContent)
