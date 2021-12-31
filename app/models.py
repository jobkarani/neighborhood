from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def save_loc(self):
        self.save()

    def __str__(self):
        return self.name


class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(Uswe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    @classmethod
    def delete_hood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def find_hood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    @classmethod()
    def update_hood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod()
    def update_occupants(cls, occupants_count):
        cls.objects.filter(occupants_count=occupants_count).update()
