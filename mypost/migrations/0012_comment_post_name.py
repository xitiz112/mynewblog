# Generated by Django 3.2.4 on 2022-04-06 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0011_auto_20220406_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mypost.post'),
        ),
    ]
