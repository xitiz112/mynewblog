# Generated by Django 3.2.4 on 2022-02-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
