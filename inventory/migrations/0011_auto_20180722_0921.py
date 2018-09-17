# Generated by Django 2.0.7 on 2018-07-22 03:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20180722_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.CharField(help_text='Enter the id of laptop', max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the brand name of laptop', max_length=50)),
                ('model', models.CharField(help_text='Enter the model of laptop', max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, help_text='Enter the cost of laptop', max_digits=10)),
                ('date_of_purchase', models.DateField(default=datetime.date.today, help_text='Enter the date of purchase')),
                ('status', models.CharField(choices=[('WK', 'Working'), ('OO', 'Out of Order'), ('IM', 'In Maintenance')], default='WK', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='model',
            field=models.CharField(default='Generic', help_text='Enter the model of printer', max_length=50),
        ),
        migrations.AddField(
            model_name='computer',
            name='name',
            field=models.CharField(default='Generic', help_text='Enter the brand name of printer', max_length=50),
        ),
    ]
