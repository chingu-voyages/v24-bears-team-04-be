# Generated by Django 3.1.2 on 2020-10-30 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20201030_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='election',
            new_name='elections',
        ),
    ]