#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#Test cases for numbertowordconversion

import unittest

import os 
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

import numbertowordconverter

testFunction = numbertowordconverter.convertToWord

class MyTest(unittest.TestCase):
    def test_simple_zero(self):
        """
        case: zero
        """
        inputStr ="0"
        outputStr = "\n0 = zero"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_simple_LT10(self):
        """
        case: <10
        """
        inputStr ="8"
        outputStr = "\n8 = eight"
        self.assertEqual(outputStr,testFunction(inputStr))
   
    def test_simple_BTW10and19(self):
        """
        case: 11 to 19
        """
        inputStr ="15"
        outputStr = "\n15 = fifteen"
        self.assertEqual(outputStr,testFunction(inputStr))
   
    def test_simple_GT20(self):
        """
        case: >20
        """
        inputStr ="23"
        outputStr = "\n23 = twenty three"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_advanced_power9(self):
        """
        case: n x 10**9
        """
        inputStr ="12345678901"
        outputStr = "\n12 345 678 901 = twelve billion, three hundred and forty five million, six hundred and seventy eight thousand, nine hundred and one"
        self.assertEqual(outputStr,testFunction(inputStr))
     
    def test_special_power12(self):
        """
        case: n x 10**12
        """
        inputStr ="7000000000000"
        outputStr = "\n7 000 000 000 000 = seven trillion"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_special_power6(self):
        """
        case: n x 10**6
        """
        inputStr ="223,000 019"
        outputStr = "\n223 000 019 = two hundred and twenty three million, nineteen"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_special_negative(self):
        """
        case: negative
        """
        inputStr ="-9000000"
        outputStr = "\n-9 000 000 = negative nine million"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_special_positive(self):
        """
        case: positive
        """
        inputStr ="+99000000"
        outputStr = "\n+99 000 000 = positive ninety nine million"
        self.assertEqual(outputStr,testFunction(inputStr))
    
    def test_exceptions_invalidInput_letter(self):
        """
        case: invalid input
        """
        inputStr ="112 i10"
        outputStr = "\ninvalid input"
        self.assertEqual(outputStr,testFunction(inputStr))

    def test_exceptions_invalidInput_SpChar(self):
        """
        case: special character-->invalid input
        """
        inputStr ="112-10"
        outputStr = "\ninvalid input"
        self.assertEqual(outputStr,testFunction(inputStr))
    
if __name__=="__main__":
    unittest.main(verbosity=2)
