from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Defines the possible roles
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('CUSTOMER', 'Customer'),
    )
    
    # Role field (default to CUSTOMER)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')
    
    # Helper properties for easy access and checks
    @property
    def is_admin(self):
        return self.role == 'ADMIN'
        
    @property
    def is_customer(self):
        return self.role == 'CUSTOMER'

    def __str__(self):
        return f"{self.username} ({self.role})"
# Create your models here.
