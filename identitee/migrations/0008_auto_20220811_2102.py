# Generated by Django 3.2.5 on 2022-08-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identitee', '0007_alter_identitee_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identitee',
            name='telephone',
        ),
        migrations.AddField(
            model_name='identitee',
            name='tel',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
