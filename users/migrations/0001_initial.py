# Generated by Django 3.1.7 on 2023-01-17 13:48

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
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('is_email', models.BooleanField(default=False)),
                ('is_password', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='Town/City')),
                ('county', models.CharField(blank=True, max_length=100, null=True, verbose_name='County')),
                ('post_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='Post Code')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('is_active', models.BooleanField(default=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('has_profile', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='user_images', verbose_name='User image')),
                ('instructions', models.CharField(blank=True, max_length=255, null=True)),
                ('fileType', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userimage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
