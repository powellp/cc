from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
import json
from django.http import Http404
from django.contrib.auth.models import User

class ImageCollection(APIView):


	def get(self,request):
		images = Image.objects.all()
		serializers = ImageSerializer(images,many=True)
		return Response(serializers.data)

	def post(self,request):
		serializers = ImageSerializer(data=request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status=status.HTTP_201_CREATED)
		return Response(json.dumps('error'),status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageDetail(APIView):

	def get_image(self,pk):
		try:
			image = Image.objects.get(pk=pk)
		except Image.DoesNotExist:
			image = 'Does Not Exist'
		finally:
			return image
		

	def get(self,request,pk):

		image = self.get_image(pk)
		if(image=='Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		serializers = ImageSerializer(image)
		return Response(serializers.data)

	def put(self,request,pk):
		image = self.get_image(pk)
		if(image == 'Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		serializers = ImageSerializer(image,data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status=status.HTTP_200_OK)
		return Response(json.dumps('Error'),status = status.HTTP_500_INTERNAL_SERVER_ERROR)

	def delete(self,request,pk):
		image = self.get_image(pk)
		if(image == 'Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))
		image.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class UserImage(APIView):

	def get_user(self,pk):
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			user = 'Does Not Exist'
		finally:
			return user 

	def get(self,request,pk):
		user = self.get_user(pk)
		if(user=='Does Not Exist'):
			return Response(json.dumps('Does Not Exist'))

		images = Image.objects.filter(user=user)
		serializers = ImageSerializer(images,many=True)
		return Response(serializers.data)