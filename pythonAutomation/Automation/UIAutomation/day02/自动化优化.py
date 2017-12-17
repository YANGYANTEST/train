import unittest
import HTMLTestRunner
class TestMethods(unittest.TestCase):
    def setUp(self):
        print("init by setUp...")

    def tearDown(self):
        print('end by tearDown...')

    def test_lupper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_2isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_3split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])

if __name__=='__main__':
    test_cass=unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    test_suit=unittest.TestSuite()
    test_suit.addTests(test_cass)
    test_result=unittest.TextTestRunner(verbosity=2).run(test_suit)
    print("testsRun:%s"%test_result.testsRun)
    print("faliures: %s" %len(test_result.failures))
    print("errors:%s"%len(test_result.skipped))
