# Generated by Django 3.2.5 on 2021-07-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='image',
            field=models.ImageField(null=True, upload_to='lungs/'),
        ),
    ]