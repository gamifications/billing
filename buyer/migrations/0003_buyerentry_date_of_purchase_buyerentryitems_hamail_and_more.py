# Generated by Django 4.0.3 on 2022-03-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerentry',
            name='date_of_purchase',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='buyerentryitems',
            name='hamail',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer',
            name='mobile2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
