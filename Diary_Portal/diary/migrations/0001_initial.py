# Generated by Django 3.0.2 on 2020-02-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=100)),
                ('CPOC', models.CharField(max_length=100)),
                ('POC', models.CharField(max_length=100)),
                ('Remarks', models.TextField()),
            ],
        ),
    ]
