# Generated by Django 2.2.11 on 2020-03-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200324_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hotwaterstatus',
            field=models.CharField(default='f', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sanitarystatus',
            field=models.CharField(default='t', max_length=200, null=True),
        ),
    ]
