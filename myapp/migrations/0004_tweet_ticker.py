# Generated by Django 4.1.1 on 2023-04-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tweet_sa_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='ticker',
            field=models.TextField(default='pizuo'),
            preserve_default=False,
        ),
    ]
