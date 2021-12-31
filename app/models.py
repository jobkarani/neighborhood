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
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

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

    @classmethod
    def update_hood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def update_occupants(cls, occupants_count):
        cls.objects.filter(occupants_count=occupants_count).update()


class User(models.Model):
    name = models.CharField(max_length=20)
    profile_pic = CloudinaryField('image')
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    about = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def create_business(self):
        self.save()

    def update_business(self):
        self.update()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models. CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def create_contact(self):
        self.save()

    def update_contact(self):
        self.update()

    def delete_contact(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        contact = cls.objects.filter(name__icontains=search_term)
        return contact

    @classmethod
    def find_contact(cls, id):
        contact = cls.objects.get(id=id)
        return contact

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def find_post(cls, id):
        post = cls.objects.get(id=id)
        return post

    class Meta:
        ordering = ['-date_created']

    def _str_(self):
        return self.name
