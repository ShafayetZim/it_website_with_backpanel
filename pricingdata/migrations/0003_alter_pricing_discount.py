# Generated by Django 4.1.3 on 2023-02-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricingdata', '0002_pricing_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='discount',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]