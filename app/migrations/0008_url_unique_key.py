# Generated by Django 2.1.7 on 2019-03-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_url_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='unique_key',
            field=models.BigIntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]