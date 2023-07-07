# Generated by Django 3.2.4 on 2023-07-07 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20230707_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='requisition_no',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='trans_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 12, 13, 59, 655087)),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='requisition_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 12, 13, 59, 655087)),
        ),
    ]