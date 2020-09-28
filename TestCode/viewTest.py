import unittest
import view
from datetime import date

class viewTest(unittest.TestCase):

    def test_viewappointment1(self):
        date=2020,7,10
        result=view.viewappointment(date)
        self.assertEqual(result,"Have appointment today")
    def test_viewappointment2(self):
        date=2020,6,9
        result=view.viewappointment(date)
        self.assertEqual(result, "Have appointment today")
    def test_viewappointment3(self):
        date=2020,7,25
        result=view.viewappointment(date)
        self.assertEqual(result, "Have appointment today")
    def test_viewappointment4(self):
        date=2020, 7, 2
        result=view.viewappointment(date)
        self.assertEqual(result, "No appointment today")
    def test_calci(self):
        d0=date(2020,7,20)
        d1=date(2020,7,26)
        result = view.calci(d0,d1,1200,1500,2,250)
        self.assertEqual(result,5700)
    def test_set(self):
        self.assertEqual(view.set(),"pass")
    def test_remove1(self):
        result=view.remove(12)
        self.assertEqual(result,"removed")
    def test_remove2(self):
        result=view.remove(15)
        self.assertEqual(result,"not found")



if __name__=="__main__":
    unittest.main()