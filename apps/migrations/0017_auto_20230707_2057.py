# Generated by Django 3.2.4 on 2023-07-07 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_auto_20230707_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='trans_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 20, 57, 32, 820713)),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='requisition_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 20, 57, 32, 820713)),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='requisition',
            field=models.CharField(max_length=100),
        ),
    ]
