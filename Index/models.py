from django.db import models

# Create your models here.
class Comment(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    comment = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.comment

class contactlist(models.Model):
    address = models.TextField(max_length=800, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.email

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)
    def __str__(self):
        return self.email

class Upload(models.Model):
    name = models.CharField(max_length=100, blank=False)
    Image = models.ImageField(upload_to="Upload", blank=False)
    link = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name
