# Generated by Django 2.0.7 on 2018-07-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20180717_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
