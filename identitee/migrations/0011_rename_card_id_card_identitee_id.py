# Generated by Django 3.2.5 on 2022-08-11 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identitee', '0010_rename_numero_card_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_id',
            new_name='identitee_id',
        ),
    ]
