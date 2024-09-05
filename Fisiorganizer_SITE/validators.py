from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    reg = re.compile("(\d{2}\d[8-9]{1}\d{8})")
    if not reg.match(value) :
        raise ValidationError(f'{value} não é um número de telefone válido')