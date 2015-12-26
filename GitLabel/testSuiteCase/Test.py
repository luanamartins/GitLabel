import unittest

# http://pyunit.sourceforge.net/pyunit.html
class Test(unittest.TestCase):

    def test(self):
        self.assertTrue(True, "ok")
    
    def testToFail(self):
        self.assertFalse(False, "not ok")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()