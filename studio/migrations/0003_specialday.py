# Generated by Django 2.0.3 on 2018-03-08 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('studio', '0002_auto_20180308_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('close_datetime', models.DateTimeField(verbose_name='Day on which studio is closed')),
                ('reason', models.CharField(max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studio.Service')),
            ],
            options={
                'db_table': 'special_off_days',
            },
        ),
    ]
