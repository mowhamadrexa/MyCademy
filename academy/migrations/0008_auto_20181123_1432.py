# Generated by Django 2.1.3 on 2018-11-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_auto_20181122_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_datetime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_datetime',
            field=models.TimeField(),
        ),
    ]
