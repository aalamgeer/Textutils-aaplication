# Generated by Django 2.1.3 on 2019-05-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicebuy', '0002_auto_20190502_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
