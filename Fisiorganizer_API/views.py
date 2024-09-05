from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response
from Fisiorganizer_SITE.models import Patient
from Fisiorganizer_API.serializers import CustomerSerializer



@api_view(['GET'])
def get_customer_by_id(request, id):
    customers = Patient.objects.filter(id=id)
    serializer = CustomerSerializer(customers, many=True)
    print(id)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_customers(request):
    customers = Patient.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_customer(request):
    print('passei pelo POST')
    pass
