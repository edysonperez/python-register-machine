import os
import sys

def EXIT():
	os.system("clear")
	print "        \n\n****THANK YOU FOR USING REGISTER MACHINE 3.0****\n\n"
	sys.exit()

def CLEAN_SCREEN():	
	os.system("clear")

def MAIN_MENU():
	print "1. -Add an item"
	print "2. -Sell Articles"
	print "3. -Exit"
	ENTER = VERIFY_VALID_CHOISE()
	CUTING(ENTER)

def VERIFY_VALID_CHOISE():
	RANGE = True
	while RANGE == True:
		ENTER = VALID_CHOISE()
		ENTER = VERIFY_INTERGER(ENTER)
		RANGE = VERIFY(ENTER)
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

def VERIFY(ENTER):
	if type(ENTER) == int:
		RANGE = False
	else:
		RANGE = True
	return RANGE

def CUTING(ENTER):
	RANGE = True
	while RANGE == True:
		MSG = VALID_NUMBER(ENTER)
		RANGE = CUT(MSG)
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

if __name__ == "__main__":
	MAIN_MENU()




