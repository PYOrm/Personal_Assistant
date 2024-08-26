from django.db import models

from users.models import User


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    body_tag = models.CharField(max_length=20, unique=True, null=False, blank=False) 

    def __str__(self):
        return self.body_tag

class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='notes')

    def __str__(self):
        return self.body[:50]
