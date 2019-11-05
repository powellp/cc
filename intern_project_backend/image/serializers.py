from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
	id = serializers.CharField(read_only=True)

	class Meta:
		model = Image
		fields = ('id','user','image')