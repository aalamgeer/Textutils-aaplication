from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)
    sub_category = models.CharField(max_length=50, null=True)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600, null=True)
    pub_date = models.DateField(null=True)
    image = models.ImageField(upload_to='nicebuy/images', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=25, default="")
    desc = models.CharField(max_length=600, default="")

    def __str__(self):
        return self.name
