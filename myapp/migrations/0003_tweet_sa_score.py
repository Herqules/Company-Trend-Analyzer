# Generated by Django 4.2 on 2023-04-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_add_default_value_to_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='sa_score',
            field=models.FloatField(default=0),
        ),
    ]