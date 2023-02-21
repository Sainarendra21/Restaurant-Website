from django.db import models

# Create your models here.

class Size(models.Model):
	title=models.CharField(max_length=100)
#to display the title in admin panel i.e small,medium,large
	def __str__(self):
		return self.title

class Pizza(models.Model):
	topping1=models.CharField(max_length=100)
	topping2=models.CharField(max_length=100)
	size=models.ForeignKey(Size,on_delete=models.CASCADE)

