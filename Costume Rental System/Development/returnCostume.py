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

def getValidID(mainData):

    """Here, we are validating the ID of costumes."""
    
    validId = False
    while validId == False:
        ID = input("Enter the costume ID to return: ")
        if ID.isdigit():
            ID = int(ID)
            if ID > 0 and ID <= len(mainData):
                validID = True
                return ID
                break    
            else:
                print("Your number is out of the options provided.")
                print("\n")
        else:
            print("Please type a number next time.")
            print("\n")

    

def getValidReturnQuantity(mainData,ID):

    """we are validating the quantity of costume to be rented."""
    returnCart = []
    
    validQuad = False
    while validQuad == False:
        quantity = input("Enter the quantity you wanna return: ")
        if quantity.isdigit():
            quantity = int(quantity)
            validQuad = True
            mainData[ID][3] = str(int(mainData[ID][3]) + quantity)
            returnCart.append([mainData[ID][0], mainData[ID][1], mainData[ID][3]])
            return quantity
        else:
            print("Please enter a number not anything else!")
            print("\n")

    
def returnCostume():

    """This function is executed when the user wants to rent the costumes."""
    
    userReturnsClothes = True
    returnCart = []
    
    while userReturnsClothes == True:
        print(printCostumes(mainData))
        ID = getValidID(mainData)
        quantity = getValidReturnQuantity(mainData,ID)

        flag = True
        for costume in returnCart:
            if costume[0] == ID:
                costume[1] += quantity
                flag = False
        if flag:
            returnCart.append([mainData[ID][0], mainData[ID][1], mainData[ID][2], quantity])

        valid_input = False
        while valid_input == False:
            returnAnother = input("Wanna return more(yes/no)? ")
            if returnAnother.lower() == "yes":
                print("\n")
                valid_input = True
                break
            elif returnAnother.lower() == "no":
                print("\n")
                generateReturnBill(returnCart)
                userReturnsClothes = False
                valid_input = True
            else:
                print("Please enter a option from given options only!")
                print("\n")
                continue 
        updateTextFile(mainData)
        print("\n")

def generateReturnBill(returnCart):
    
    """Here, we are generating the return bill in the shell as well as in txt formate."""
    
    validName = False
    while validName == False:
        Name = str(input("Please enter your name: "))
        if Name.replace(" ", "").isalpha():
            validName = True
        else:
            print("Sorry, You mistakely typed your name wrong!")
            print("\n")
            
    validDay = False
    while validDay == False:
        day = input("Enter number of Day from rent days: ")
        if day.isdigit():
            day = int(day)
            validDay = True
        else:
            print("Please enter the days which is always in number!")
            print("\n")       
          
    validPhoneNumber = False
    while validPhoneNumber == False:
        phoneNumber = str(input("Enter your Phone Number: "))
        if phoneNumber.isdigit():
            validPhoneNumber = True
        else:
            print("Sorry, You mistakely typed your Phone Number wrong!")
            print("\n")
    
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
    print("----------------------------------------------Return Bill-------------------------------------------------")
    print(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    print(f"Customer Name: {Name}")
    print(f"Phone Number: {phoneNumber}")
    print("---------------------------------------------------------------------------------------------------------")
    print("S.No.", "\t\t", "Costume Name", "\t\t", "Brand", "\t\t\t", "Price", "\t\t", "Quantity")
    print("---------------------------------------------------------------------------------------------------------")
    row = ""
     
    counter = 0

    if day > 5:
        newDay = day - 5
        fine = newDay*5
    else:
        fine = 0
    
    for i in range(len(returnCart)):
        counter += 1
        for j in range(len(returnCart[i])):
            row = row + str(returnCart[i][j]) + "\t\t"    
        print(counter,"\t\t",row)
        row = ""
            
    print("---------------------------------------------------------------------------------------------------------")
    print(f"                                             Fine: ${fine}                                       ")
    print("---------------------------------------------------------------------------------------------------------")
    print("                                    Thank you for vising our store                                       ")
    print("                                           Visit again :)                                                ")
    print()
    print("-------------------------------Bill has also been generated in txt file.---------------------------------")

 
    #This code prints the bill in txt formate.
    text = f"Return-{Name}.txt"
    file = open(text,"w")
    file.write("------------------------------------------Costume Rental Shop--------------------------------------------")
    file.write("\n")
    file.write("                                           Kathmandu, Nepal                                              ")
    file.write("\n")
    file.write(f"                                             GST.NO:-{GST}                                              ")
    file.write("\n")
    file.write("---------------------------------------------Return Bill-------------------------------------------------")
    file.write("\n")
    file.write(f"Date:- {Year}-{Month}-{Day}                                                               Time:- {Hour}:{Minute}:{Second}:{microSecond}")
    file.write("\n")
    file.write(f"Customer Name: {Name}")
    file.write("\n")
    file.write(f"Phone Number: {phoneNumber}")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("S.No. \t\t Costume Name \t\t Brand \t\t Price \t\t Quantity")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    row = ""
     
    counter = 0
    finalPrice = 0
    for i in range(len(returnCart)):
        counter += 1
        for j in range(len(returnCart[i])):
            row = row + str(returnCart[i][j]) + "\t\t\t"   
        file.write(f"{counter} \t\t {row}")
        file.write("\n")
        row = ""
            
    file.write("---------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"                                    Fine: ${fine}                                          ")
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
