# Generated by Django 2.0.7 on 2018-07-17 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20180717_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='date_of_purchase',
            field=models.DateField(default=datetime.date.today, help_text='Enter the date of purchase'),
        ),
    ]