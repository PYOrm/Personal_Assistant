from django.db import models
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=255)
    date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ed_info = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    