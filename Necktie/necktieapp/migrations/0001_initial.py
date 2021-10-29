# Generated by Django 3.2.8 on 2021-10-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_surnam', models.CharField(blank=True, max_length=20, null=True)),
                ('d_firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('d_username', models.CharField(max_length=40, unique=True)),
                ('d_phone', models.IntegerField(blank=True, null=True)),
                ('d_address', models.TextField(blank=True, null=True)),
                ('d_country', models.CharField(max_length=30)),
                ('d_state', models.CharField(choices=[('CD', 'Cardiology'), ('GS', 'General Surgery'), ('EC', 'Endocrinology'), ('NT', 'Neonatology')], max_length=4)),
                ('d_pincode', models.IntegerField()),
            ],
        ),
    ]
