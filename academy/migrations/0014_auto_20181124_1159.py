# Generated by Django 2.1.3 on 2018-11-24 16:59

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0013_auto_20181123_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='RFID_code',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='class',
            name='color1',
            field=colorfield.fields.ColorField(default=1, max_length=18),
        ),
        migrations.AlterField(
            model_name='class',
            name='color2',
            field=colorfield.fields.ColorField(default=5, max_length=18),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=5000),
        ),
    ]