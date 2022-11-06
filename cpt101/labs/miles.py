# Program to convert miles to Kilometers
# Created by Kevin Soule
# Date: 8/24/2017

print("Welcome to my distance convertor") #welcome message
print("I can convert miles to kilometers")

choice = 'y'
miles_to_kilo = 0.621  #convertion rate for miles to kilometers

while choice == 'y':    #begin loop , indented until end
    miles = float(input("Please enter miles:   "))  #input read strings
                #taking result from input and sending to float function
    kilo = miles * miles_to_kilo
    print("Equvalent kilometers =   ",kilo)
    choice = input("Convert more (y/n):   ")  #last line of loop, ends indent
    
print() #blank line
print("Thank you for using my Program!")

print("Last Conversion: ",miles," miles to ",kilo, " kilometers")
    #example of multiple outputs
