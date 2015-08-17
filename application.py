import os
import sys

def EXIT():
    CLEAN_SCREEN()
    print "        \n\n****THANK YOU FOR USING REGISTER MACHINE 3.0****\n\n"
    sys.exit()

def CLEAN_SCREEN():
    os.system("clear")

def MAIN_MENU():
    print "1. -Add an item"
    print "2. -Sell Articles"
    print "3. -Exit"
    ENTER = VERIFY_VALID_CHOISE()
    VERIFY_VALID_NUMBER(ENTER)

def VERIFY_VALID_CHOISE():
    RANGE = True
    while RANGE == True:
        ENTER = VALID_CHOISE()
        ENTER = VERIFY_INTERGER(ENTER)
        RANGE = VERIFY_TYPE_INTEGER(ENTER)
    return ENTER

def VALID_CHOISE():
    ENTER = raw_input("Enter number from 1 to 3 please\n>")
    return ENTER

def VERIFY_INTERGER(ENTER):
    try:
        ENTER = int(ENTER)
        return ENTER
    except ValueError:
        return "INVALID"

def VERIFY_TYPE_INTEGER(ENTER):
    if type(ENTER) == int:
        RANGE = False
    else:
        RANGE = True
    return RANGE

def VERIFY_VALID_NUMBER(ENTER):
    RANGE = True
    while RANGE == True:
        MSG = VALID_NUMBER(ENTER)
        RANGE = SELECT_CHOISE(MSG)
        if RANGE == True:
            ENTER = VERIFY_VALID_CHOISE()

def VALID_NUMBER(ENTER):
    if ENTER < 1 or ENTER > 3:
        MSG = "INVALID_RANGE"
        print MSG
    else:
        MSG = CORRECT_NUMBER(ENTER)
    return MSG

def CORRECT_NUMBER(ENTER):
    if ENTER == 1:
        OPTION_ONE(ENTER)
        ENTER_PRODUCTS(ENTER)

    elif ENTER == 2:
        OPTION_TWO(ENTER)
        print "OPTION_TWO"
    elif ENTER == 3:
        OPTION_THREE(ENTER)
        EXIT()
       
def OPTION_ONE(ENTER):
    return "OPTION_ONE"

def OPTION_TWO(ENTER):
    return "OPTION_TWO"

def OPTION_THREE(ENTER):
    return "OPTION_THREE"   

def SELECT_CHOISE(MSG):
    if MSG == "OPTION_ONE" or MSG == "OPTION_TWO" or MSG == "OPTION_THREE":
        RANGE = False
    else:
        RANGE = True
    return RANGE

def ENTER_PRODUCTS(ENTER):        
    ITEMS = {}
    BOX = True
    while BOX == True:
        SELECT = raw_input("You wish to enter a product y/n: ")
        try:
            if SELECT.isalpha() == True:
                if SELECT.lower() == "y":
                    PRODUCT = raw_input("Enter Product: ")
                    PRICE = int(raw_input("Enter Price: "))
                    ITEMS[PRODUCT] = PRICE
                elif SELECT.lower() == "n":
                    BOX = False
                else:
                    print "Unrecognized data"
            else:
                print "Non numerical data are recognized"
        except:
            BOX = True
    print "Your items are: "
    for KEY in ITEMS:
        print KEY,":",ITEMS[KEY]    

if __name__ == "__main__":
    MAIN_MENU()