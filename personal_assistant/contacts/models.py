from django.db import models
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=255)
    date = models.DateField(null=True, blank=True) 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ed_info = models.TextField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_contact(cls, name, email, owner, address=None, phone=None, date=None, ed_info=None):
        """
        Create and return a new contact instance.
        """
        contact = cls(name=name, address=address, phone=phone, email=email, date=date, owner=owner, ed_info=ed_info)
        contact.save()
        return contact

    def update_contact(self, **kwargs):
        """
        Update the fields of the contact instance.
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    @classmethod
    def delete_contact(cls, contact_id):
        """
        Delete a contact by its ID.
        """
        contact = cls.objects.get(id=contact_id)
        contact.delete()

    @classmethod
    def get_contact(cls, contact_id):
        """
        Retrieve a contact by its ID.
        """
        return cls.objects.get(id=contact_id)
    