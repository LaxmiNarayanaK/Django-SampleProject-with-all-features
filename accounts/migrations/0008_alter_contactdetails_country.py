# Generated by Django 4.0.1 on 2022-02-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_contactdetails_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetails',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('United States', 'United States')], default='IN', max_length=20),
        ),
    ]