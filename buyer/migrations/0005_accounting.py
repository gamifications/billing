# Generated by Django 4.0.3 on 2022-03-28 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_rename_hamail_buyerentryitems_hamali'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_credit', models.BooleanField(default=False)),
                ('date_of_entered', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer')),
            ],
        ),
    ]