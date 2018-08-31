import sta
import unittest

strArr = 'a dsf sd rw as;   '

class TestFirst(unittest.TestCase):
	def test(self):
		self.assertEqual(sta(strArr)[0], 'a')

class TestLast(unittest.TestCase):
	def test(self):
		self.assertEqual(sta(strArr)[4], 'as;')

class TestLength(unittest.TestCase):
	def test(self):
		self.assertEqual(len(sta(strArr)), 5)

if __name__ == '__main__':
    unittest.main()
