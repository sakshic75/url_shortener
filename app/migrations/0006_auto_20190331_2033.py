# Generated by Django 2.1.7 on 2019-03-31 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190330_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
        migrations.AddField(
            model_name='url',
            name='unique_id',
            field=models.BigIntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
