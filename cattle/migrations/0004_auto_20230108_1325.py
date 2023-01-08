# Generated by Django 3.2.5 on 2023-01-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0003_rename_cattle_id_stable_cattle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stable',
            name='cattle',
        ),
        migrations.AddField(
            model_name='stable',
            name='address',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='stable',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
