# Generated by Django 3.2.5 on 2023-01-08 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stable', '0001_initial'),
        ('cattle', '0005_cattle_stable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='stable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stable.stable'),
        ),
        migrations.DeleteModel(
            name='Stable',
        ),
    ]
