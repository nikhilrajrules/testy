# Generated by Django 3.0.3 on 2020-07-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200722_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joiners',
            name='test_uid',
            field=models.CharField(default=0, help_text='Enter Your Test ID', max_length=10),
        ),
    ]