# Generated by Django 2.0.10 on 2019-02-23 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_survey_pi_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinformation',
            old_name='country_of_resedence',
            new_name='country_of_residence',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='pi_set',
        ),
    ]
