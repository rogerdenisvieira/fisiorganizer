from django.forms import ValidationError
from django.test import TestCase
from Fisiorganizer_SITE.validators import validate_phone

class ValidatorsTest(TestCase):
    
    def test_invalid_phone(self):
        
        self.assertRaises(ValidationError, validate_phone('123456789'))
