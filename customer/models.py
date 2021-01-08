from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class Testimonial(models.Model):
	customer = models.CharField(max_length=50, blank=True)
	profession = models.CharField(max_length=50, blank=True)
	testimony = models.TextField(max_length=300, blank=True)

	def __str__(self):
		return self.customer
	