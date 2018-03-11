# Generated by Django 2.0.3 on 2018-03-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('full_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('contact_number', models.CharField(max_length=20, verbose_name='contact number of client')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
