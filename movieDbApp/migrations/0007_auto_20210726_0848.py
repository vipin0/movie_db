# Generated by Django 3.2.5 on 2021-07-26 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieDbApp', '0006_alter_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(default=0, verbose_name='Average Rating'),
        ),
        migrations.AddField(
            model_name='movie',
            name='numeber_rating',
            field=models.IntegerField(default=0, verbose_name='Total Reviews'),
        ),
    ]
