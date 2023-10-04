from django.db import models
from userapp.models import Agent
# Create your models here.


class Property(models.Model):
    # Property Details
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    sqft = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Location
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    property_pics = models.ImageField(upload_to='property_pics/', blank=True)
    
    # Agent Relationship
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    
    def __str__(self):
        return self.title
