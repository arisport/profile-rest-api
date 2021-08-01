from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format = None):
        """Return a list of ApiView Features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete',
            'Is similar to tranditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to Urls'
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk= None):
        """Handle updating an object"""
        """pk should not be none as is should be passes as parameter to update specific model"""
        return Response({'method': "put"})

    def patch(self, request, pk= None):
        """Handle partial updating an object"""
        """pk should not be none as is should be passes as parameter to update specific model"""
        return Response({'method': "patch"})
    
    def delete(self, request, pk= None):
        """Delete an object"""
        """pk should not be none as is should be passes as parameter to update specific model"""
        return Response({'method': "delete"})





