ENTER = 0
def	VALUE_CHOISE(ENTER = 0):
	#print "Estoy en VALUE_CHOISE"
	NOT_LETTERS = True
	while NOT_LETTERS == True:
		ENTER = raw_input("Enter number from 1 to 3 please\n>")
		if ENTERINT(ENTER) == True:
			NOT_LETTERS = False
		else:
			print "Enter only numbers please"
			NOT_LETTERS = True
	CORRECT_NUMBER (int(ENTER))
	return ENTER

def ENTERINT(ENTER):
	#print "Estoy en ENTERINT"
	try:
		ENTER = int(ENTER)
		return True
	except ValueError:
		return False

def CORRECT_NUMBER(ENTER):
	#print "Estoy en CORRECT_NUMBER"
	if ENTER == 1:
		print "Selecciono la opcion 1"
	elif ENTER == 2:
		print "Selecciono la opcion 2" 	
	elif ENTER == 3:
		print "Selecciono la opcion 3"

def MENUPRI(ENTER):
	print "1. -Add an item"
	print "2. -Sell Articles"
	print "3. -Exit"
	VALUE_CHOISE()

if __name__ == "__main__":
	MENUPRI(ENTER)
