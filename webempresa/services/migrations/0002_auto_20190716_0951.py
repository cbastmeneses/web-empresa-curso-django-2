# Generated by Django 2.2.2 on 2019-07-16 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='update',
            new_name='updated',
        ),
    ]