# Generated by Django 3.2.7 on 2021-09-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Duration',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]