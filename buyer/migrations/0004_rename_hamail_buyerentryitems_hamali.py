# Generated by Django 4.0.3 on 2022-03-28 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_buyerentry_date_of_purchase_buyerentryitems_hamail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyerentryitems',
            old_name='hamail',
            new_name='hamali',
        ),
    ]
