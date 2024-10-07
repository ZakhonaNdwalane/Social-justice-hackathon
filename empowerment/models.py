from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class FinancialService(models.Model):
    LOAN = 'loan'
    GRANT = 'grant'
    INSURANCE = 'insurance'

    SERVICE_TYPES = [
        (LOAN, 'Loan'),
        (GRANT, 'Grant'),
        (INSURANCE, 'Insurance'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    service_type = models.CharField(max_length=100, choices=SERVICE_TYPES)
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class WealthInitiatives(models.Model):
    initiative_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional field
    funding_goal = models.DecimalField(max_digits=12, decimal_places=2)
    funds_raised = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    beneficiaries = models.IntegerField() # Optional field
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.initiative_name

    def clean(self):
        # Ensure that funds_raised cannot exceed the funding_goal
        if self.funds_raised > self.funding_goal:
            raise ValidationError('Funds raised cannot exceed the funding goal.')
        
        # Ensure that the start_date is before the end_date
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError('Start date cannot be after end date.')

    def save(self, *args, **kwargs):
        self.clean()
        super(WealthInitiatives, self).save(*args, **kwargs)

class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class LoginForm(models.Model): 
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
