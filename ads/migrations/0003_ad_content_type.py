# Generated by Django 3.1 on 2020-09-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True),
        ),
    ]
