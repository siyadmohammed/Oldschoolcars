# Generated by Django 5.0.1 on 2024-04-02 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
    ]