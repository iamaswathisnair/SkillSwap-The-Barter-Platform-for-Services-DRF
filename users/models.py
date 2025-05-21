from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('company_owner', 'Company Owner'),
        ('legal_team', 'Legal Team'),
        ('investigator', 'Investigator'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)  # For soft delete

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    
    
# 💡 Why did you use this CustomUser?
# Because in your project (ZeroLeak), different users do different jobs:

# Role	        What They Do
# employee	    Bound by NDA, could leak stuff (😈 maybe)
# company_owner	Can upload NDAs, track cases
# legal_team	Confirms if something is really a breach, closes legal cases
# investigator	Investigates reports, flags suspicious employees

# So, you need to identify them by role.
