# Generated by Django 5.1.1 on 2024-09-05 12:48

import Fisiorganizer_SITE.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fisiorganizer_SITE', '0010_remove_patient_age_patient_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='phone',
            field=models.CharField(max_length=13, validators=[Fisiorganizer_SITE.validators.validate_phone]),
        ),
    ]
