from django.db import models


# Create your models here.

class Forex(models.Model):
    currency = models.TextField()
    buy = models.DecimalField(max_digits=7, decimal_places=2)
    sell = models.DecimalField(max_digits=7, decimal_places=2)
    last_update = models.DateField(auto_now_add=True)


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    img_url = models.TextField()
    small_img_url = models.TextField()
    title = models.TextField()
    fulltext = models.TextField()
    date = models.TextField()
    updated = models.DateField(auto_now=True)
