# Generated by Django 3.2.8 on 2021-10-27 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0003_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.CreateModel(
            name='PatentDoctorTb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='necktieapp.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='necktieapp.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ManyToManyField(through='necktieapp.PatentDoctorTb', to='necktieapp.Doctors'),
        ),
    ]
