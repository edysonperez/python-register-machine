import application
import unittest

class test_REGISTER_MACHINE(unittest.TestCase):
	def test_ENTER_INT(self):
		self.assertEqual(application.ENTER_INT("h"),"INVALID")
		self.assertEqual(application.CORRECT_NUMBER(1),"OPTION_ONE")
		self.assertEqual(application.CORRECT_NUMBER(2),"OPTION_TWO")
		self.assertEqual(application.CORRECT_NUMBER(3),"OPTION_THREE") 
		self.assertEqual(application.VALID_NUMBER(0),"INVALID_RANGE")
		self.assertEqual(application.VALID_NUMBER(4),"INVALID_RANGE")

if __name__ == "__main__":
	unittest.main()