# Generated by Django 3.2.8 on 2021-12-24 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20211224_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='phone_num',
            new_name='phone_number',
        ),
    ]
