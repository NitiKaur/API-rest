from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIview featues"""
        an_apiview = [
        'uses HTTP methods as function(get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives you the most control over your application logic',
        'is mapped manually to URLs',
        ]

        return Response({'message': 'hello!','an_apiview': an_apiview})
