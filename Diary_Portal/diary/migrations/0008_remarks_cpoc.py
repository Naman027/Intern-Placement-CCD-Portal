# Generated by Django 3.0.2 on 2020-02-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_remarks_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='remarks',
            name='CPOC',
            field=models.CharField(default='NULL', max_length=100),
            preserve_default=False,
        ),
    ]
