# Generated by Django 2.2 on 2020-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powerconsumptionrate',
            name='Powerwater',
        ),
        migrations.AddField(
            model_name='powerbase',
            name='Powerwater',
            field=models.FloatField(default=0.0, max_length=20, verbose_name='全厂制水电耗'),
        ),
    ]
