from rest_framework.views import APIView
from rest_framework.response import Response
class HelloApiView(APIView):
    """Test Api View"""

    def get(self,request,format = None):
        """Return a list of ApiView Features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete',
            'Is similar to tranditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to Urls'
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})
