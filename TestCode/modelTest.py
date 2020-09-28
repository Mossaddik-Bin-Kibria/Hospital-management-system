import unittest
import model

class modelTest(unittest.TestCase):

    def test_search_button1(self):
        patientID=16221001
        result = model.search_button(patientID)
        self.assertEqual(result, "Patient is found")

    def test_search_button2(self):
        patientID=16221002
        result = model.search_button(patientID)
        self.assertEqual(result, "Patient is found")

    def test_search_button3(self):
        patientID=16221003
        result = model.search_button(patientID)
        self.assertEqual(result, "Patient is found")
    def test_search_button4(self):
        patientID=16221050
        result = model.search_button(patientID)
        self.assertEqual(result, "Patient is not found")
    def test_search_button6(self):
        patientID=177755
        result = model.search_button(patientID)
        self.assertEqual(result, "Patient is found")
    def test_PAT(self):
        self.assertEqual(model.PAT(), "pass")
        self.assertEqual(model.PAT(), "fail")
    def test_delete_button(self):
        self.assertEqual(model.Delete_button(101), "Employee deleted")
        self.assertEqual(model.Delete_button(102), "Employee deleted")
        self.assertEqual(model.Delete_button(103), "Employee ID not found")
    def test_P_UPDATE(self):
        self.assertEqual(model.P_UPDATE(501), "Patient updated")
        self.assertEqual(model.P_UPDATE(502), "Patient updated")
        self.assertEqual(model.P_UPDATE(103), "Patient not found")
    def test_IN_PAT(self):
        self.assertEqual(model.IN_PAT(), "Patient values updated")
    def test_P_UPDATE(self):
        self.assertEqual(model.P_UPDATE(), "Patient update screen successful")
    def test_D_display(self):
        self.assertEqual(model.D_display(), "Delete window successful")
    def test_menu(self):
        self.assertEqual(model.menu(), True)

if __name__=="__main__":
    unittest.main()



