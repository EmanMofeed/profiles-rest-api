from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of APIView Feature"""
        an_apiview = [
        'Uses HTTP method as function (get, post,patch,put,delete)',
        'Is similer to a traditional Django View',
        'Gives you the most control over you application login',
        'it mapped manaually to URls'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
