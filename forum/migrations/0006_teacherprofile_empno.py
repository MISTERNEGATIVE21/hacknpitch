# Generated by Django 3.2.7 on 2021-09-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_issue_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='empno',
            field=models.CharField(default='', max_length=255),
        ),
    ]
