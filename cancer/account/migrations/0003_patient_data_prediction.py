# Generated by Django 3.2.5 on 2021-07-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_patient_data_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='prediction',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
