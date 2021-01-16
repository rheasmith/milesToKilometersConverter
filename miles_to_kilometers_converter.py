##############################
## Program: Lab 02
## Author: Rhea Smith
## Date: 07/05/2020
## Description: This program will prompt the user for a distance in miles or kilometers
##              and will convert that distance to the opposite unit (miles or kilometers).
## Input: choice, miles, kilometers, convertToMi, convertToKm
## Output: newMiles, newKilometers
##
## Psuedocode:
## display choice "Is your distance in miles (m) or kilometers (k)?"
## input m or k
##
## input miles
## define convertToKm
## set newKilometers = miles * convertToKm
## display "That's", newKilometers, "kilometers!"
##
## input kilometers
## define convertToMi
## set newMiles = kilometers * convertToMiles
## display "That's", newMiles, "miles!"
##
## display "Invalid entry. Please type m for miles or k for kilometers."
## input m or k (repeat options)
##
## input miles
## define convertToKm
## set newKilometers = miles * convertToKm
## display "That's", newKilometers, "kilometers!"
##
## input kilometers
## define convertToMi
## set newMiles = kilometers * convertToMiles
## display "That's", newMiles, "miles!"


## User choice of calculator option (m or k)
choice = input("Is your distance in miles (m) or kilometers (k)? ")

##
if choice == "m":
    ## Miles to Kilometers
    miles = float(input("Enter the distance in miles: "))
    convertToKm = 1.60934
    newKilometers = miles * convertToKm
    print("That's", newKilometers, "kilometers!")

elif choice == "k":

    ## Kilometers to Miles
    kilometers = float(input("Enter the distance in kilometers: "))
    convertToMi = 0.621371
    newMiles = kilometers * convertToMi
    print("That's", newMiles, "miles!")

else:
    print("Invalid entry. Please type m for miles or k for kilometers.")

    ## User choice of calculator option (m or k)
    choice = input("Is your distance in miles (m) or kilometers (k)? ")

    ##
    if choice == "m":
        ## Miles to Kilometers
        miles = float(input("Enter the distance in miles: "))
        convertToKm = 1.60934
        newKilometers = miles * convertToKm
        print("That's", newKilometers, "kilometers!")

    elif choice == "k":
        ## Kilometers to Miles
        kilometers = float(input("Enter the distance in kilometers: "))
        convertToMi = 0.621371
        newMiles = kilometers * convertToMi
        print("That's", newMiles, "miles!")
