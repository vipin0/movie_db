# Generated by Django 3.2.5 on 2021-07-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieDbApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('about', models.CharField(max_length=255, verbose_name='About')),
                ('website', models.URLField(verbose_name='Website')),
            ],
            options={
                'verbose_name': 'StreamingPlatform',
                'verbose_name_plural': 'StreamingPlatforms',
            },
        ),
    ]