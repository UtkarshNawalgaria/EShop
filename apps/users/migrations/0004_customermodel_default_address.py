# Generated by Django 3.1.4 on 2021-01-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_address_default'),
        ('users', '0003_customermodel_addresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='default_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.address'),
        ),
    ]
