# Generated by Django 3.0.4 on 2020-04-24 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0010_auto_20200422_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='duration',
            field=models.DecimalField(decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Период выполнения'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='fines',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='Комментарий'),
        ),
    ]
