# Generated by Django 2.1.3 on 2019-05-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicebuy', '0005_auto_20190511_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
