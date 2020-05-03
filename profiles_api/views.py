from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models


from profiles_api import permissions

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

class HelloViewSet(viewsets.ViewSet):

    serializer_class= serializers.HelloSerializers
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
        'uses actions (list, create , retrieve, update , partial update)'
        'Automatically maps URLs using Routers'
        ] 

        return Response({'message':'Hello','a_viewset':a_viewset})
    # Create your views here.

    def create(self,request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})



    def partial_update(self, request,pk=None):
        """Handle partially updating an object"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request,pk=None):
        """Handle deletion of an object"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


