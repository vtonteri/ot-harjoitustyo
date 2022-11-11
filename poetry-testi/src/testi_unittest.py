import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = 'hello kulli'
        self.assertEqual(s.split(), ['hello', 'kulli'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(0)

if __name__ == '__main__':
    unittest.main()