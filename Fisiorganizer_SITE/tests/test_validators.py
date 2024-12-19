from django.forms import ValidationError
from django.test import TestCase
import Fisiorganizer_SITE
from Fisiorganizer_SITE.validators import validate_phone

class ValidatorsTest(TestCase):
    
    def test_invalid_phone(self):
        self.assertRaises(ValidationError, validate_phone, '0000000000')

    def test_empty_phone(self):
        self.assertRaises(ValidationError, validate_phone, '')
    
    def test_short_phone(self):
        self.assertRaises(ValidationError, validate_phone, '21')

    def test_too_long_phone(self):
        self.assertRaises(ValidationError, validate_phone, '1234561324544223454')        

    def test_mock(self):
        self.assertTrue(True)
