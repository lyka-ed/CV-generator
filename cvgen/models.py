from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    work_experience = models.TextField(max_length=1000)
    technical_skills = models.TextField(max_length=1000)
    soft_skills = models.TextField(max_length=1000)