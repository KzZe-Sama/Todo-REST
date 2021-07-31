from django.db.models.query import QuerySet
from rest_framework.response import Response
from .serializers import AddressDetailsSerializer,UserSerializer
from rest_framework import generics, serializers
from .models import User,AddressDetails
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# Create your views here.

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self,request):
        querySet = self.get_queryset()
        serializer = UserSerializer(querySet,many=True)
        return Response(serializer.data)
    
