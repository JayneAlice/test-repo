# Generated by Django 4.2.16 on 2024-11-15 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_osoba_options_alter_stanowisko_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osoba',
            old_name='data_dodanie',
            new_name='data_dodania',
        ),
    ]
