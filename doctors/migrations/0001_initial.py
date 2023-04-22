# Generated by Django 4.2 on 2023-04-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_no', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('client_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('suregon', 'suregon'), ('nuerologist', 'nuerologist')], max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
