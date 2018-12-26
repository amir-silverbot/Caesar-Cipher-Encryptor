#gathering inputs
inputString = input("Enter your string: ")
print("\n")
stringLength = len(inputString)
shift = input("Enter shift [default is 3]: ")
print("\n")
outputString = ""
newASCII = 0
if (str.isdigit(shift) == False):
    shift = 3
    print("Shift has been set to 3 because of bad input...\n")
#watch out for out of range shifts!
shift = int(shift) % 26

for i in range(stringLength):
    
    #uppercase characters
    if (ord(inputString[i]) >= 65 and ord(inputString[i]) <= 90):
        if ((ord(inputString[i]) + shift) > 90):
            newASCII = ((ord(inputString[i]) + shift) % 90) + 64
        else:
            newASCII = ord(inputString[i]) + shift
        outputString += chr(newASCII)
                                          
    #lowercase characters
    elif (ord(inputString[i]) >= 97 and ord(inputString[i]) <= 122):
        if ((ord(inputString[i]) + shift) > 122):
            newASCII = ((ord(inputString[i]) + shift) % 122) + 96
        else:
            newASCII = ord(inputString[i]) + shift
        outputString += chr(newASCII)

    #remaining characters
    else:
        outputString += chr(ord(inputString[i]))

#print outputString
print("Encrypted string is: " + outputString)
print("\n")
input("Press enter to continue...")
