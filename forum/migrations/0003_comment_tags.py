# Generated by Django 3.2.7 on 2021-09-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_issue_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]
