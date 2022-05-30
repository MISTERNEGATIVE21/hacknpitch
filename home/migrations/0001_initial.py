# Generated by Django 3.2.7 on 2021-09-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactModel",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.BigIntegerField(blank=True)),
                ("message", models.TextField()),
            ],
        ),
    ]
