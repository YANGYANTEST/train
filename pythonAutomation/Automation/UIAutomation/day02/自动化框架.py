import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def tes_isupper(self):
        self.assertEqual('Foo'.isupper())

    def test_split(self):
        mystr='hello world'
        self.assertEqual(mystr.split(),['hello','world'])

if __name__ =='__main__':
    #unittest.main  为测试提供了入口
    unittest.main()