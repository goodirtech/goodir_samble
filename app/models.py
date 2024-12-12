from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
   


class JobCategory(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.category_name
    

class Village(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    # Village ID will be auto-generated as the primary key
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')


    def __str__(self):
        return self.name
    
class Technician(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    # Technician details
    name = models.CharField(max_length=100)
    job_role = models.ForeignKey(JobCategory, on_delete=models.PROTECT, related_name="technichian")  # e.g., electrician, plumber
    address = models.ForeignKey(Village, on_delete=models.PROTECT, related_name='technician',  null=True)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    image = models.ImageField(upload_to='technician_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.name} - {self.job_role}"

    class Meta:
        ordering = ['name']

class Client(models.Model):
    CLIENT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name= models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.ForeignKey(Village, on_delete=models.SET_NULL, blank=True, null=True, related_name="clients")
    status = models.CharField(max_length=10, choices=CLIENT_STATUS_CHOICES, default='not_paid')
    description= models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    
class Job(models.Model):
    # Django will automatically add a unique `id` field as the primary key
    
    JOB_STATUS_CHOICES = [
         ('process', 'Process'),
        ('complete', 'Complete'),
    ]
    # Customer details
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_address = models.ForeignKey(Village, on_delete=models.PROTECT, related_name='jobs',  null=True)

    # Job details
    job_category = models.ForeignKey(JobCategory, on_delete=models.PROTECT, related_name="jobs", null=True)
    job_description = models.TextField(blank=True)

    # Technician details
    technician_name = models.ForeignKey(Technician, on_delete=models.PROTECT,related_name="jobs", null=True)
    

    # Financial details
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    technician_salary = models.DecimalField(max_digits=10, decimal_places=2)

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=8, choices=JOB_STATUS_CHOICES, default='process')
    


    class Meta:
        ordering = ['-created_at']

class ClientJob(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,  # Prevents deletion of Client if referenced in ClientJob
        related_name='jobs'
    )
    created_at = models.DateTimeField(default=timezone.now)  # Default to now but can be manually set
    updated_at = models.DateTimeField(default=timezone.now) 
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    technician_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_category = models.ForeignKey(JobCategory, on_delete=models.PROTECT, related_name="clientJobs", null=True)
    job_description = models.TextField(blank=True)

    # Technician details
    technician_name = models.ForeignKey(Technician, on_delete=models.PROTECT,related_name="clientJobs", null=True)
    PAID_STATUS = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    status = models.CharField(max_length=6, choices=PAID_STATUS, default='unpaid')

    def __str__(self):
        return f"{self.client} - {self.get_status_display()}"
    
   
        

