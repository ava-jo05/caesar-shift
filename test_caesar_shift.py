import unittest
from caesar_shift import decrypt_shift, decrypt_unknown_shift, encrypt, find_shift

class TestCaesarShift(unittest.TestCase):
    def test_encrypt_1(self):
        self.assertEqual(encrypt("ABC", 3), 'DEF')
    def test_encrypt_2(self):
        self.assertEqual(encrypt("XYZ", 26), "XYZ")
    def test_encrypt_3(self):
        self.assertEqual(encrypt("hello", 29), "KHOOR")
    def test_encrypt_4(self):
        self.assertEqual(encrypt("Hello, World!", 7), "OLSSV, DVYSK!")

    def test_decrypt_shift_1(self):
        self.assertEqual(decrypt_shift("DEF", 3), 'ABC')
    def test_decrypt_shift_2(self):
        self.assertEqual(decrypt_shift("XYZ", 26), "XYZ") 
    def test_decrypt_shift_3(self):
        self.assertEqual(decrypt_shift("khoor", 29), "HELLO")  
    def test_decrypt_shift_4(self):
        self.assertEqual(decrypt_shift("OLSSV, DVYSK!", 7), "HELLO, WORLD!")
    
    def test_find_shift_1(self):
        self.assertEqual(find_shift("RHCPC"), {2, 17}) # THERE, 2
    def test_find_shift_2(self):
        self.assertEqual(find_shift("YNYFSNH"), {24, 5, 20}) # TITANIC, 5
    def test_find_shift_3(self):
        self.assertEqual(find_shift("NNEQINEX"), {9, 6, 13}) # AARDVARK, 13
    def test_find_shift_4(self):
        self.assertEqual(find_shift("WHD WLPH!"), {18, 3, 22}) # TEA TIME!, 3
    
    def test_decrypt_unknown_shift_1(self):
        self.assertEqual(decrypt_unknown_shift("PANNW"), ["GREEN", "CNAAJ", "JUHHQ"])
    def test_decrypt_unknown_shift_2(self):
        self.assertEqual(decrypt_unknown_shift("RUBK RKZZKX"), ["ILSB IBQQBO", "HKRA HAPPAN", "LOVE LETTER"])
    def test_decrypt_unknown_shift_3(self):
        self.assertEqual(decrypt_unknown_shift("NBDCPPL"), ["CQSREEA", "JXZYLLH", "YMONAAW"])
    def test_decrypt_unknown_shift_4(self):
        self.assertEqual(decrypt_unknown_shift("PEEATHPJRT"), ["ETTPIWEYGI", "LAAWPDLFNP", "APPLESAUCE"])

if __name__ == '__main__':
    unittest.main()