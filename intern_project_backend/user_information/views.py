from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers
from .models import UserInformation
from django.contrib.auth.models import User 
from django.http import Http404
from django.contrib.auth import authenticate
import json

class UserCollection(APIView):

	def get(self,request):
		users = User.objects.all()
		serializers = UserSerializers(users,many=True)
		return Response(serializers.data)

	def post(self,request):
		serializers = UserSerializers(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status = status.HTTP_201_CREATED)
		return Response(json.dumps("Enter a new username "))

class UserDetail(APIView):

	def get_user(self,pk):
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			user = 'Does Not Exist'
		finally:
			return user

	def get(self,request,pk):
		user = self.get_user(pk)
		if(user == 'Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		serializers = UserSerializers(user)
		return Response(serializers.data)

	def post(self,request,pk):
		user = self.get_user(pk)
		if(user == 'Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		data = request.data
		serializers = UserSerializers(user,data=data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data)
		return Response(json.dumps('Error updating information'))

	def delete(self,request,pk):
		user = self.get_user(pk)
		if (user == 'Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		user.delete()
		return Response(status.HTTP_204_NO_CONTENT)

class UserAuth(APIView):

	def post(self,request):
		username = request.data['username']
		password = request.data['password']
		user = authenticate(username=username,password=password)
		if user:
			serializers = UserSerializers(user)
			return Response(serializers.data,status=status.HTTP_200_OK)
		return Response(json.dumps("Enter username/password again"))

class UserSearch(APIView):

	def post(self,request):
		username = request.data['username']
		users = User.objects.filter(username__icontains=username)
		serializers = UserSerializers(users,many=True)
		return Response(serializers.data)