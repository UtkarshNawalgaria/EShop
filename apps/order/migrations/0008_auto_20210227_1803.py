# Generated by Django 3.1.4 on 2021-02-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210202_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]