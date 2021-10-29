# Generated by Django 3.2.8 on 2021-10-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0005_auto_20211028_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ManyToManyField(blank=True, null=True, through='necktieapp.PatentDoctorTb', to='necktieapp.Doctors'),
        ),
    ]