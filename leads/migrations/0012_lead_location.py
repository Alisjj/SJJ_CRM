# Generated by Django 3.2.8 on 2021-12-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_rename_phone_num_lead_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='location',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]