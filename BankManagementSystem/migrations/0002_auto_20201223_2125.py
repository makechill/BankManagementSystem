# Generated by Django 3.1.4 on 2020-12-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagementSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banksss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='BankDetails',
        ),
    ]