# Generated by Django 3.2.9 on 2022-06-01 10:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_coursemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=14, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='price by $(dollar)'),
        ),
    ]
