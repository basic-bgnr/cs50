# Generated by Django 2.1.2 on 2018-10-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20181006_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timedatabase',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='TimeZone',
        ),
    ]
