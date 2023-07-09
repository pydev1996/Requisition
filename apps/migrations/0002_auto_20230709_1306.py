# Generated by Django 3.2.4 on 2023-07-09 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='join_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='primary_email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='secondary_email',
        ),
        migrations.AlterField(
            model_name='issue',
            name='trans_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 13, 6, 38, 203567)),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='requisition_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 13, 6, 38, 203567)),
        ),
    ]