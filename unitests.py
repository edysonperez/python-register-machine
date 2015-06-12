from application import ASK_ENTER
import unittest

class Test_ASK_ENTER(unittest.TestCase):
	def Test_ASK_ENTER(self):
		self.assertTrue(ASK_ENTER("h") == True)
		self.assertTrue(ASK_ENTER(0) == False)
		#self.assertEqual(ASK_ENTER(1),1)
		#self.assertEqual(ASK_ENTER(2),2)
		#self.assertEqual(ASK_ENTER(3),3) 

if __name__ == "__main__":
	unittest.main()