# Generated by Django 3.2.5 on 2022-08-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identitee', '0008_auto_20220811_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]