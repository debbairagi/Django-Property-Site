from django.db import models

# Create your models here.

class ContactUSMessage(models.Model):
    # Sender Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    # Message Details
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"