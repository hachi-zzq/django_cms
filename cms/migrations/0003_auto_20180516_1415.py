# Generated by Django 2.0.5 on 2018-05-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20180516_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='status',
            field=models.CharField(default='NORMAL', max_length=70),
        ),
    ]
