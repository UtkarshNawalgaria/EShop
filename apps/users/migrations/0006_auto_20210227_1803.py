# Generated by Django 3.1.4 on 2021-02-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210126_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='VendorModel',
        ),
    ]