##################################################################
# Script Name: BV_Assignment8.py
# Title: Assignment 8.
# Description: Code file for SCP220 Week 8 Assignment.
# IDE of your choice: VScode.
# Author: Bernie Valderrama
# Date:  March 9th, 2024
##################################################################
from os import system, name
from time import sleep as sl

class Car():
    def __init__(self, make, model, vin, mileage, price, features = []):
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        self.features = features
    
    def toString(self):
        data = f'Make: {self.make}\nModel: {self.model}\nMileage: {self.mileage}\nVIN: {self.vin}\nPrice: {self.price}\nFeatures: \n'
        for feat in self.features:
            data += "\t" + feat + "\n"
        return data
    
def clearScreen():
    if name == "nt":
        system("cls")
    else: 
        system("clear")

def printMenu():    # Week 8 - modified printMenu to display 2 additional options
    clearScreen()
    print("====================Inventory Manager======================")
    print("1. Add vehicle")
    print("2. Edit vehicle")
    print("3. Remove vehicle")
    print("4. Print list of vehicles")
    print("5. Save inventory to file")          
    print("6. Load inventory from file")    
    print("7. Print list of vehicles in ascending order - based on VIN")
    print("8. Print list of vehicles in descending order - based on VIN")    
    print("9. Quit menu")

def enterInteger(): # Week 8 - function handles exception if user does not enter an integer (ValueError)
    while True:
        val = input("Please enter a value: ")
        try:
            val = int(val)
            break
        except ValueError:
            val = print(val, "is not a number. Please enter a number.")
    return val

def enterString():  # Week 8 - function handles exception if user does not enter a string (ValueError)
    while True:
        val = input("Please enter a value: ")
        try:
            if val.isdigit():
                raise ValueError
            break
        except ValueError:
            val = print(val, "is a number. Please enter a set of characters.")
    return val

def addVehicle():
    clearScreen()
    print("++++++++++++++++++++++++ Add Vehicle ++++++++++++++++++++++++")
    print("Enter the vehicle information when prompted.\n")        
        
    print("Capturing the vehicle's Make")
    make = enterString()

    print("Capturing the vehicle's Model")
    model = enterString()

    print("Capturing the vehicle's VIN")
    vin = enterInteger()

    print("Capturing the vehicle's Mileage")
    mileage = enterInteger()

    print("Capturing the vehicle's Price")
    price = enterInteger()

    features = []
    print("Enter each feature one at a time, press Enter twice to end:")
    feat = input()
    while (feat != ""):
        features.append(feat)
        feat = input()
    vehicle_inventory.append(Car(make, model, vin, mileage, price, features))

def editVehicle():
    printVehicles(2)
    targetVin = input("Enter the VIN of the vehicle you wish to edit: ")
    index = 0
    found = False
    for car in vehicle_inventory:
        if car.vin == targetVin:
            index = vehicle_inventory.index(car)
            found = True
    
    if found:
        for key in vehicle_inventory[index].__dict__:
            if key == "features":
                features = []
                print("Enter each feature one at a time, press Enter twice to end:")
                feat = input()
                while (feat != ""):
                    features.append(feat)
                    feat = input()
                vehicle_inventory[index].__dict__[key] = features
            else:
                val = input(key + ":")
                if val != "":
                    vehicle_inventory[index].__dict__[key] = val
    else: 
        input("Error, no vehicle found with that VIN number. \nPress Enter to return to menu...")

def removeVehicle():
    printVehicles(2)
    targetVin = input("Enter the VIN of the vehicle you wish to remove: ")
    index = 0
    found = False
    for car in vehicle_inventory:
        if car.vin == targetVin:
            index = vehicle_inventory.index(car)
            found = True
    
    if found:
        choice = input(f'Are you sure you wish to remove this vehicle?:\n{vehicle_inventory[index].toString()}')
        if choice[0].lower() == 'y':
            vehicle_inventory.remove(vehicle_inventory[index])
        else: 
            input("Vehicle was NOT removed. Press Enter to return to menu...")
    else: 
        input("Error, no vehicle found with that VIN number. \nPress Enter to return to menu...")

def printVehicles(mode):
    if mode == 1:
        clearScreen()
        for car in vehicle_inventory:
            print(car.toString())
        input("Press Enter to continue...")
    elif mode == 2:
        clearScreen()
        for car in vehicle_inventory:
            print(car.toString())
    else: 
        clearScreen()
        for car in vehicle_inventory:
            print(car.toString())
        input("Press Enter to continue...")

def saveToFile():                               
    filename = input("Saving inventory to file - Please enter the file name: ")
    with open(filename, "w") as outfile:
        for car in vehicle_inventory:
            outfile.write(f'{car.make},{car.model},{str(car.vin)},{str(car.mileage)},{str(car.price)},')
            counter = 1
            for feature in car.features:
                if counter < len(car.features):
                    outfile.write(f'{feature},')
                    counter += 1
                else:
                    outfile.write(f'{feature}')            
            outfile.write("\n")

def minToMaxSort():    # Week 8 - Feature Option - Displaying list of vehicles from min to max based on VIN
    vinList = []

    for car in vehicle_inventory:
        vinList.append(int(car.vin))

    counter = 0
    while counter != len(vinList):
        for i in range (counter,len(vinList)):
            if vinList[i] < vinList[counter]:
                vinList[counter],vinList[i] = vinList[i],vinList[counter]
        counter += 1
    displaySortedListBasedOnVin(vinList)

def maxToMinSort():    # Week 8 - Feature Option - Displaying list of vehicles from max to min based on VIN
    vinList = []

    for car in vehicle_inventory:
        vinList.append(int(car.vin))

    counter = 0
    while counter != len(vinList):
        for i in range (counter,len(vinList)):
            if vinList[i] > vinList[counter]:
                vinList[i],vinList[counter] = vinList[counter],vinList[i]
        counter += 1
    displaySortedListBasedOnVin(vinList)

def displaySortedListBasedOnVin(L): # Week 8 - Feature Option - Displaying list of vehicles after sorting (min-to-max or max-to-min)
    clearScreen()
    counter = 0
    while counter < len(vehicle_inventory):
        for car in vehicle_inventory:
            if L[counter] == int(car.vin):
                print(car.toString(), end="")
        counter += 1
    input("Press Enter to continue...")

def loadFromFile():     # Week 8 - loadFromFile function with exception handling (FileNotFound & EOFE - file is empty)
    while True:                                                              
        filename = input("Loading inventory from file - Please enter the file name: ")
        try:
            with open(filename) as infile:
                temp = infile.readline() 
                if temp == "":
                    raise EOFError
                else:
                    with open(filename) as thisfile:
                        for line in thisfile:
                            vls = line.split(",")
                            vehicle_inventory.append(Car(vls[0], vls[1], vls[2], vls[3], vls[4], list(vls[5:])))
            break
        except FileNotFoundError:
            print("\nA file with that name does not exist. Please try again.")
        except EOFError:
            print("\nFile exists, but it contains no data.")

vehicle_inventory = []
def main():
    prompt = "Enter your choice from above: "
    choice = 0;
    while(choice != 9):
        printMenu()
        choice = int(input(prompt))
        if choice == 1:
            addVehicle()
            prompt = "Enter your choice from above: "
        elif choice == 2:
            editVehicle()
            prompt = "Enter your choice from above: "
        elif choice == 3:
            removeVehicle()
            prompt = "Enter your choice from above: "
        elif choice == 4:
            printVehicles(1)
            prompt = "Enter your choice from above: "
        elif choice == 5:       
            saveToFile()
            prompt = "Enter your choice from above: "
        elif choice == 6:
            loadFromFile()      
            prompt = "Enter your choice from above: "
        elif choice == 7:
            minToMaxSort()
            prompt = "Enter your choice from above: "
        elif choice == 8:
            maxToMinSort()
            prompt = "Enter your choice from above: "
        elif choice == 9:
            clearScreen()
            print("Good Bye!")
            sl(3)
        else: 
            prompt = "Invalid Entry: enter the number operation #, then press enter: "
        
main()