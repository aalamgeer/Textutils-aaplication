# Generated by Django 2.1.3 on 2019-05-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nicebuy', '0008_auto_20190518_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=25)),
                ('desc', models.CharField(default='', max_length=600)),
            ],
        ),
    ]