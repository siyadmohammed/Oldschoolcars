# Generated by Django 5.0.1 on 2024-04-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=150),
        ),
    ]