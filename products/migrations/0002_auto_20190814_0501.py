# Generated by Django 2.2.4 on 2019-08-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
