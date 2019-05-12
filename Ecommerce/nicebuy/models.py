from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)
    sub_category = models.CharField(max_length=50, null=True)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, null=True)
    pub_date = models.DateField(null=True)
    image = models.ImageField(upload_to='nicebuy/images', default="")

    def __str__(self):
        return self.product_name
