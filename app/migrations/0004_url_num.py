# Generated by Django 2.1.7 on 2019-03-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_url_j'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='num',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
