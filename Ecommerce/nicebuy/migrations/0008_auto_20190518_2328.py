# Generated by Django 2.1.3 on 2019-05-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicebuy', '0007_auto_20190512_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='nicebuy/images'),
        ),
    ]
