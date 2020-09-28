import unittest
import controller

class controllerTest(unittest.TestCase):

    def test_login_function1(self):
         result = controller.login_function('admin','12345')
         self.assertEqual(result, "pass")


    def test_login_function2(self):
         result = controller.login_function('admin','1234')
         self.assertEqual(result, "fail")

    def test_login_function3(self):
         result = controller.login_function('','')
         self.assertEqual(result, "fail")

if __name__=="__main__":
    unittest.main()