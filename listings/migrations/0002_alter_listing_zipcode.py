# Generated by Django 4.0.3 on 2022-03-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]