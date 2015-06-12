def ASK_ENTER():
	ENTER = raw_input("Enter number from 1 to 3 please\n>")
	return ENTER

def ENTERINT(ENTER):
	#print "Estoy en ENTERINT"
	try:
		ENTER = int(ENTER)
		CORRECT_NUMBER(ENTER)
		return False
	except ValueError:
		return True

def CORRECT_NUMBER(ENTER):
	#print "Estoy en CORRECT_NUMBER"
	if ENTER == 1:
		print "Selecciono la opcion 1"
	elif ENTER == 2:
		print "Selecciono la opcion 2" 	
	elif ENTER == 3:
		print "Selecciono la opcion 3"

def MENUPRI():
	print "1. -Add an item"
	print "2. -Sell Articles"
	print "3. -Exit"
	NOT_LETTERS = True
	while NOT_LETTERS == True:
		ENTER = ASK_ENTER()
		NOT_LETTERS = ENTERINT(ENTER)
		
if __name__ == "__main__":
	MENUPRI()
