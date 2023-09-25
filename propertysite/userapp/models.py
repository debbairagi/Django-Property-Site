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

# class Property(models.Model):
#     # Property Details
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     bedrooms = models.PositiveIntegerField()
#     bathrooms = models.PositiveIntegerField()
#     sqft = models.PositiveIntegerField()
#     lot_size = models.DecimalField(max_digits=10, decimal_places=2)
    
#     # Location
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=10)
    
#     # Agent Relationship
#     agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    
#     def __str__(self):
#         return self.title

