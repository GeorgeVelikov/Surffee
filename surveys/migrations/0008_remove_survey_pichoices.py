# Generated by Django 2.0.10 on 2019-02-23 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_auto_20190223_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='pichoices',
        ),
    ]
