# Generated by Django 3.1.14 on 2022-03-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temperature',
            field=models.FloatField(blank=True, default=0.1, max_length=10, null=True, verbose_name='코덱스온도'),
        ),
    ]