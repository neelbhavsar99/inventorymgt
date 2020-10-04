from django.db import models


# Create your models here; store data
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    fullname = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    SKUNum = models.IntegerField(max_length=200)
    BarcodeNum = models.IntegerField(max_length=200)
    Month = models.IntegerField(max_length=200)


class TrainingModel(models.Model):
    sales = models.DecimalField(decimal_places=2, max_digits=250)
    label = models.DecimalField(decimal_places=2, max_digits=250)
    cost = models.DecimalField(decimal_places=2, max_digits=250)
    msrp = models.DecimalField(decimal_places=2, max_digits=250)
    month = models.IntegerField(max_length=2)
    mon = models.IntegerField(max_length=200)
    tues = models.IntegerField(max_length=200)
    wed = models.IntegerField(max_length=200)
    thurs = models.IntegerField(max_length=200)
    fri = models.IntegerField(max_length=200)
    sat = models.IntegerField(max_length=200)
    sun = models.IntegerField(max_length=200)


class StoreData(models.Model):
    sales = models.DecimalField(decimal_places=2, max_digits=250)
    cost = models.DecimalField(decimal_places=2, max_digits=250)
    msrp = models.DecimalField(decimal_places=2, max_digits=250)
    month = models.IntegerField(max_length=2)
    mon = models.IntegerField(max_length=200)
    tues = models.IntegerField(max_length=200)
    wed = models.IntegerField(max_length=200)
    thurs = models.IntegerField(max_length=200)
    fri = models.IntegerField(max_length=200)
    sat = models.IntegerField(max_length=200)
    sun = models.IntegerField(max_length=200)
    SKU = models.IntegerField(max_length=200)