from django.db import models


# Create your models here.

class ContactMe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    budget = models.PositiveBigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    attachment = models.FileField(blank=True, null=True, upload_to='contact_me_attachment')

    def __str__(self):
        return f"Id: {self.pk}, Name: {self.name}"
