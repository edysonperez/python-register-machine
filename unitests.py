from application import VALID_CHOISE
import unittest

class Test_VALID_CHOISE(unittest.TestCase):
	def Test_VALID_CHOISE(self):
		self.assertEqual(VALID_CHOISE("h"),"INVALID")
		self.assertEqual(VALID_CHOISE(1),"OPTION_ONE")
		self.assertEqual(VALID_CHOISE(2),"OPTION_TWO")
		self.assertEqual(VALID_CHOISE(3),"OPTION_THREE") 
		self.assertEqual(VALID_CHOISE(0),"INVALID_RANGE")
		self.assertEqual(VALID_CHOISE(4),"INVALID_RANGE")

if __name__ == "__main__":
	unittest.main()