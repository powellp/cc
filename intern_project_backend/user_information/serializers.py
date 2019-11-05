from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import UserInformation

class UserSerializers(serializers.ModelSerializer):

	id = serializers.CharField(read_only=True)
	mobile_number = serializers.CharField(source = 'user_information.mobile_number')
	address = serializers.CharField(source = 'user_information.address')

	class Meta:
		model = User
		fields = ('id','username','password','mobile_number','address')
		extra_kwargs = {'password' : {'write_only' : True}}

	def create(self,validated_data):
		user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
		UserInformation.objects.create(user=user,mobile_number=validated_data['user_information']['mobile_number'],address=validated_data['user_information']['address'])
		return user
