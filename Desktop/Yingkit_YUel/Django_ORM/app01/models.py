from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    pub_time = models.DateField()
    author = models.CharField(max_length=32, null=True)
    waijian = models.ForeignKey('publisher',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)


class publisher(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    publish = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
