# Generated by Django 3.2.5 on 2023-01-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0004_auto_20230108_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='cattle',
            name='stable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cattle.stable'),
        ),
    ]
