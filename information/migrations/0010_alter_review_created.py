# Generated by Django 4.1.2 on 2023-07-13 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0009_alter_review_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 0, 57, 8, 254042)),
        ),
    ]