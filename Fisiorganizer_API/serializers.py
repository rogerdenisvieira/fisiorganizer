from rest_framework import serializers
from Fisiorganizer_SITE.models import Patient


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'