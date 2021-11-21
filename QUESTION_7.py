#*At least 1 letter between [a-z] and 1 letter between [A-Z]. -- done
#*At least 1 number between [0-9]. -- done
#*At least 1 special character [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]. -- done
#*Minimum length 6 characters. -- done
#*Maximum length 16 characters. -- done

def printGuidlines():
    print("Here are the guidelines for a password")
    print("*At least 1 letter between [a-z] and 1 letter between [A-Z].")
    print("*At least 1 number between [0-9].")
    print("*At least 1 special character.")
    print("*Minimum length 6 characters.")
    print("*Maximum length 16 characters.")

def checkLength(password):
    if(6 <= len(password) <= 16):
        return True
    return False

def checkLowerCase(password):
    for c in password:
        if(97 <= ord(c) <= 122):
            return True
    return False

def checkUpperCase(password):
    for c in password:
        if(65 <= ord(c) <= 90):
            return True
    return False

def checkNumericCharacter(password):
    for c in password:
        if(48 <= ord(c) <= 57):
            return True
    return False

def checkSpecialCharacter(password):
    for c in password:
        if(33 <= ord(c) <= 47):
            return True
        elif(58 <= ord(c) <= 64):
            return True
        elif (91 <= ord(c) <= 96):
            return True
        elif (123 <= ord(c) <= 126):
            return True
    return False

def checkAllConditions(password):
    flag = checkLength(password) and checkLowerCase(password) and checkUpperCase(password) and checkNumericCharacter(password) and checkSpecialCharacter(password)
    return flag

def main():
    printGuidlines()
    password = input("Please type in your password: ")

    while(not checkAllConditions(password)):
        print("The password you have entered does not comply with the guidelines.")
        print("Please try again.")
        printGuidlines()
        password = input("Please type in your password: ")

    print(password)


if __name__ == '__main__':
    main()