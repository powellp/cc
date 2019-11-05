from django.db import models
from django.contrib.auth.models import User 

class Image(models.Model):
	user = models.ForeignKey(User,related_name='user_image',on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'portfolio_image',blank=True,max_length=255,null=True)

	def __str__(self):
		return str(self.user)
