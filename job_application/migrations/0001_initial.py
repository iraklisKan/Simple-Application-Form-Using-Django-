# Generated by Django 5.2.4 on 2025-07-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField()),
                ('occupation', models.CharField(max_length=100)),
            ],
        ),
    ]
