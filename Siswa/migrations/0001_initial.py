# Generated by Django 4.1.2 on 2023-01-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_siswa', models.CharField(max_length=5)),
                ('nama', models.CharField(max_length=20)),
                ('usia', models.IntegerField()),
                ('nama_wali', models.CharField(max_length=20)),
            ],
        ),
    ]
