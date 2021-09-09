# Generated by Django 3.2.7 on 2021-09-09 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='Anonymous', max_length=255)),
                ('reputation', models.IntegerField(default=0)),
                ('rollno', models.CharField(default='', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='(Not available)', max_length=100)),
                ('summary', models.TextField(default='(Not available)', max_length=200)),
                ('description', models.TextField(default='(Not available)', max_length=750)),
                ('image', models.ImageField(blank=True, upload_to='forum/images/')),
                ('tracked', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('status', models.TextField(default='', max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(default='Anonymous', max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('votes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-votes', '-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('username', models.CharField(default='Anonymous', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='testing', max_length=255)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
