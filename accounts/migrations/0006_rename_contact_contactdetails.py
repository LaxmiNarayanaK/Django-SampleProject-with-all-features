# Generated by Django 4.0.1 on 2022-02-21 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contactdetails',
        ),
    ]
