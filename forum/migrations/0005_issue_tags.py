# Generated by Django 3.2.7 on 2021-09-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210914_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.JSONField(default=dict),
        ),
    ]
