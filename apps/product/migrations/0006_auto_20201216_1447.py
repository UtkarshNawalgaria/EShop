# Generated by Django 3.1.4 on 2020-12-16 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='long_description',
        ),
    ]
