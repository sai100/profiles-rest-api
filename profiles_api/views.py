from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Return a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to traditional Django View',
            'Gives most control over app logic',
            'is manually mapped to urls'
        ]

        return Response({'message': 'Hello World', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hellow message with our name'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''returns a hello message'''

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partially_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': "Hello!", 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new hello message'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handle getting an object by ID'''

        return Response({'http_method': "GET"})

    def update(self, request, pk=None):
        '''Handle updating an object by ID'''

        return Response({'http_method': "PUT"})

    def partial_update(self, request, pk=None):
        '''Handle updating partially part of an object by ID'''

        return Response({'http_method': "PATCH"})

    def destroy(self, request, pk=None):
        '''Handle removing an object by ID'''

        return Response({'http_method': "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handles creating and updating profiles'''

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
