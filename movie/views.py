import requests
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

from django.core import serializers

from django.shortcuts import render

from requests.auth import HTTPBasicAuth
  
@api_view(['GET',]) 
@permission_classes([IsAuthenticated])
def movies(request):
		data=requests.get('https://demo.credy.in/api/v1/maya/movies/',
		auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',
			'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
		return Response(data.json())


@api_view(['POST',])
def registration(request):
	if request.method=='POST':
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			user = User.objects.get(username=serializer.validated_data['username']) 
			token, created = Token.objects.get_or_create(user=user)


			return Response({'access_token': token.key})

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)