# Generated by Django 3.1.7 on 2023-01-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.FileField(upload_to='user_images', verbose_name='User image'),
        ),
    ]
