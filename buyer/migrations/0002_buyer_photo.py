# Generated by Django 4.0.3 on 2022-03-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='photo',
            field=models.ImageField(default='', upload_to='buyer/'),
            preserve_default=False,
        ),
    ]
