# Generated by Django 2.1.3 on 2019-05-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicebuy', '0003_auto_20190502_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
    ]
