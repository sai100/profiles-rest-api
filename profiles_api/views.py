from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Return a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to traditional Django View',
            'Gives most control over app logic',
            'is manually mapped to urls'
        ]

        return Response({'message': 'Hello World', 'an_apiview': an_apiview})
