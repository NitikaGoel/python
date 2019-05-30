import unittest
import cap
class Testcap(unittest.TestCase):
    def  test_one(self):
        text = 'python'
        result = cap.capi(text)
        print(result)
        self.assertEqual(result,'Python')

if __name__=='__main__':
    unittest.main()
