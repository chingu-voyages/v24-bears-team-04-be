# Generated by Django 3.1.2 on 2020-11-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0009_auto_20201101_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='locality',
            field=models.CharField(choices=[('National', (('N1', 'Nation 1'),)), ('Regional', (('R1', 'Region 1'), ('R2', 'Region 2'))), ('Local', (('D1', 'District 1'), ('D2', 'District 2')))], max_length=100, null=True),
        ),
    ]
