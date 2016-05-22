"""
Author: Andrew Schutt
File: testdie.py
Date: 9/25/09

This will test the die module
"""

from die import Die
import unittest

class TestDie(unittest.TestCase):
    """Defines the unit test for the Die class"""

    def setUp(self):
        """sets up a test fixture"""
        self._die = Die()
        
    def testRoll(self):
        """Test case for roll."""
        self.assertEquals(self._die)

    def testGetRoll(self):
        """Test case for getRoll."""
        self.assertEquals(self._die)

    def testShow(self):
        """Test case for show."""

    def testSetRoll(self):
        """Test case for setRoll."""
        self.assertEquals(self._die,3)
    
    suite = unittest.makeSuite(TestDie)
    unittest.TextTestRunner()run(suite)
