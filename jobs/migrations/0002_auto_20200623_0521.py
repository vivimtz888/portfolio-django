# Generated by Django 3.0.7 on 2020-06-23 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=300),
        ),
    ]
