# Generated by Django 3.1 on 2020-09-09 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='States',
            new_name='states',
        ),
    ]
