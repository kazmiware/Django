# Generated by Django 4.1 on 2022-10-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.CharField(default=None, max_length=20),
        ),
    ]