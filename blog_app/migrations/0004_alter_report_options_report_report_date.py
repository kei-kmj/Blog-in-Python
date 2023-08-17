# Generated by Django 4.2.4 on 2023-08-17 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-report_date']},
        ),
        migrations.AddField(
            model_name='report',
            name='report_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2023, 8, 17)),
            preserve_default=False,
        ),
    ]