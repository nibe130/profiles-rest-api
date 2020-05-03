from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HellowApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializers

    def get(self,request,format=None):
        """REturns a list  of APIView features"""

        an_apiview = ['uses HTTP methods as function (get ,post,put, patch, delete)',
        'I hope to do well']

        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """create a hello message with the passed in name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    #pk is the primary key id of the object we are updating
    def put(self,response,pk=None):
        """Handle updating objects"""
        return Response({'method':'PUT'})

    #updates partially onl the fields provided in the patch request. Ex only last name if 
    #if you use put last name the entrire object will be updated the first name will be empty
    #if you use patch the first name will be left as it is only the second name will be updated
    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle deletion of an object"""
        return Response({'method':'DELETE'})

    

    # Create your views here.
