from rest_framework.views import APIView
from rest_framework.response import Response
from Fisiorganizer_SITE.models import Customer
from Fisiorganizer_API.serializers import CustomerSerializer


class CustomerList(APIView):
    def get(self, request, id):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
