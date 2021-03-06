# Generated by Django 4.0.1 on 2022-02-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateLicensed', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Island', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.TextField()),
                ('filename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SeleniumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LegalName', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('MailingAddress', models.CharField(max_length=50)),
                ('OffsiteCultivationAddress', models.CharField(max_length=100)),
                ('ManufactureAddress', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('License', models.CharField(max_length=50)),
                ('LicenseEffective', models.CharField(max_length=50)),
                ('OwnerLicense', models.CharField(max_length=50)),
                ('Services', models.CharField(max_length=50)),
            ],
        ),
    ]
