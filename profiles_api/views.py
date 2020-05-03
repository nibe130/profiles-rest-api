from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HellowApiView(APIView):
    """Test API View"""
    
    def get(self,request,format=None):
        """REturns a list  of APIView features"""

        an_apiview = ['uses HTTP methods as function (get ,post,put, patch, delete)',
        'I hope to do well']

        return Response({'message':'Hello','an_apiview':an_apiview})
# Create your views here.
