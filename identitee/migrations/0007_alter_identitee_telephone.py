# Generated by Django 3.2.5 on 2022-08-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identitee', '0006_alter_identitee_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identitee',
            name='telephone',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
