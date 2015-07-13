import application
import unittest

class test_REGISTER_MACHINE(unittest.TestCase):
	def test_VERIFY_INTERGER(self):
		self.assertEqual(application.VERIFY_INTERGER("h"),"INVALID")
	
	def test_CORRECT_NUMBER(self):	
		self.assertEqual(application.CORRECT_NUMBERcd(1),"OPTION_ONE")
		self.assertEqual(application.CORRECT_NUMBER(2),"OPTION_TWO")
		self.assertEqual(application.CORRECT_NUMBER(3),"OPTION_THREE") 
	
	def	test_VALID_NUMBER(self):
		self.assertEqual(application.VALID_NUMBER(0),"INVALID_RANGE")
		self.assertEqual(application.VALID_NUMBER(4),"INVALID_RANGE")
	
	def test_CHOISE_ENTER_PRODUCTS(self):
		self.assertNotEqual(application.ENTER_PRODUCTS_YES_OR_NOT("y"),"ENTER_PRODUCTS") 
		self.assertNotEqual(application.ENTER_PRODUCTS_YES_OR_NOT("n"),"BACK_MENU")
		self.assertNotEqual(application.ENTER_PRODUCTS_YES_OR_NOT("STRING"),"INVALID_CHOISE")
		self.assertNotEqual(application.ENTER_PRODUCTS_YES_OR_NOT(1),"INVALID_INPUT")

if __name__ == "__main__":
	unittest.main()