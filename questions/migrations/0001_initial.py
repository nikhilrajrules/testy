# Generated by Django 3.0.3 on 2020-07-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joiners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_uid', models.CharField(default=0, help_text='Enter Your Test ID', max_length=10)),
                ('ques_used', models.IntegerField(default=0, help_text='Your Test Score')),
                ('student_emailid', models.EmailField(default='abc@abc.com', help_text='Confirm your email', max_length=254)),
                ('ques_id', models.IntegerField(default=0, help_text='Your Test Score')),
            ],
            options={
                'ordering': ['test_uid'],
            },
        ),
    ]
