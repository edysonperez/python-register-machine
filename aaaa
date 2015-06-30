import os
import sys

def CLEAN_SCREEN():	
	os.system("clear")

def MENU_PRI():
	print "1. -Add an item"
	print "2. -Sell Articles"
	print "3. -Exit"	
	ENTER = RAN()
	CUTING(ENTER)

def RAN():
	RANGE = True
	while RANGE == True:
		ENTER = VALID_CHOISE()
		ENTER = ENTER_INT(ENTER)
		RANGE = VERIFY(ENTER)
	return ENTER

def CUTING(ENTER):
	RANGE = True
	while RANGE == True:
		MSG = VALID_NUMBER(ENTER)
		RANGE = CUT(MSG)
		if RANGE == True:
			ENTER = RAN()

def VALID_CHOISE():
	ENTER = raw_input("Enter number from 1 to 3 please\n>")
	return ENTER

def ENTER_LETTERS(ENTER):
	if ENTER.isalpha():
		return "VALID"

def ENTER_INT(ENTER):
	try:
		ENTER = int(ENTER)
		return ENTER
	except ValueError:
		return "INVALID"

def VERIFY(ENTER):
	if type(ENTER) == int:
		RANGE = False
	else:
		RANGE = True
	return RANGE

def VALID_NUMBER(ENTER):
	if ENTER < 1 or ENTER > 3:
		MSG = "INVALID_RANGE"
		print MSG
	else:
		MSG = CORRECT_NUMBER(ENTER)
	return MSG

def CORRECT_NUMBER(ENTER):
	if ENTER == 1:
		return "OPTION_ONE"
	elif ENTER == 2:
		return "OPTION_TWO" 	
	elif ENTER == 3:
		EXIT()
		return "OPTION_THREE"
	
def CUT(MSG):
	if MSG == "OPTION_ONE" or MSG == "OPTION_TWO" or MSG == "OPTION_THREE":
		RANGE = False
	else:
		RANGE = True
	return RANGE
	
def EXIT():
	os.system("clear")
	if __name__ == "__main__":
		print "        \n\n****THANK YOU FOR USING REGISTER MACHINE 3.0****\n\n"
		sys.exit()

def CHOISE_ENTER_PRODUCTS(SELECT = ""):
	SELECT = raw_input("You wish to enter a product? y/n: ")
	RESPONSE = ENTER_PRODUCTS_YES_OR_NOT(SELECT)

	if a == "VALID":
		if SELECT.lower() == "y":
			pass
		elif SELECT.lower() == "n":
			pass
		else:
			return "INVALID_CHOISE"
	else:
		return "ENTER_NUMBER"


def ENTER_PRODUCTS_YES_OR_NOT(SELECT):
	a = ENTER_LETTERS(SELECT)
	if a == "VALID":
		if SELECT.lower() == "y":
			return "ENTER_PRODUCTS"
		elif SELECT.lower() == "n":
			return "BACK_MENU"
		else:
			return "INVALID_CHOISE"
	else:
		return "INVALID_INPUT"




if __name__ == "__main__":
	MENU_PRI()

