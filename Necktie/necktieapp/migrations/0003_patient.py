# Generated by Django 3.2.8 on 2021-10-27 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0002_alter_doctors_d_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_surname', models.CharField(blank=True, max_length=20, null=True)),
                ('p_fullname', models.CharField(blank=True, max_length=20, null=True)),
                ('p_username', models.CharField(max_length=40)),
                ('p_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('p_country', models.CharField(blank=True, max_length=50, null=True)),
                ('p_state', models.CharField(blank=True, max_length=50, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='necktieapp.doctors')),
            ],
        ),
    ]
