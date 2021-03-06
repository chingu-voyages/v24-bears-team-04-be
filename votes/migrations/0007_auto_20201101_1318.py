# Generated by Django 3.1.2 on 2020-11-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_auto_20201030_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='tier',
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tier', models.CharField(choices=[('Local', 'Local'), ('Regional', 'Regional'), ('National', 'National'), ('Other', 'Other')], max_length=10, null=True)),
                ('locality', models.CharField(choices=[('Local', (('D1', 'District 1'), ('D2', 'District 2'))), ('Regional', (('R1', 'Region 1'), ('R2', 'Region 2')))], max_length=100, null=True)),
                ('election', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.election')),
            ],
        ),
    ]
