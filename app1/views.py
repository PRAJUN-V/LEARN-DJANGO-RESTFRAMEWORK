from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status,generics
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView

from .models import ExampleModel
from .serializers import ExampleModelSerializer

# Functional based view 
@api_view(['GET','POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def example(request):
    if request.method == 'GET':
        name = {
            'name' : 'prajun'
        }
        return Response(name, status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response({'method' : 'post'})


# Class Based View
class Example2(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({
            'method' : 'get'
        })
    
    def post(self, request):
        return Response({
            'method' : 'post'
        })
    
# Generic view
class ExampleModelListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

class ExampleModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer


# implemented differnt typed of view in django restframework
