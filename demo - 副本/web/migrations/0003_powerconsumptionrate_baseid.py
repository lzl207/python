# Generated by Django 2.2 on 2020-07-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200712_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerconsumptionrate',
            name='baseid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.Powerbase', verbose_name='基础表id'),
        ),
    ]
