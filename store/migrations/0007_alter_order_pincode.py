# Generated by Django 5.0.1 on 2024-04-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
