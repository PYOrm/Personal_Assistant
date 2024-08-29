from django.db import models


# Create your models here.

class Forex(models.Model):
    currency = models.TextField()
    buy = models.DecimalField(max_digits=7, decimal_places=2)
    sell = models.DecimalField(max_digits=7, decimal_places=2)
    last_update = models.DateField(auto_now_add=True)



class News(models.Model):
    pass
