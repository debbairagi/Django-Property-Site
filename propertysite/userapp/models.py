from django.db import models

# Create your models here.


class Agent(models.Model):
    # Personal Information
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    # profile_picture = models.ImageField(upload_to='agent_profile_pics/', null=True, blank=True)
    
    # Address
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    
    # Additional Information
    biography = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


