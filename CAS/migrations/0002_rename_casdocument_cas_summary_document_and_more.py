# Generated by Django 5.0.2 on 2024-02-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cas_summary',
            old_name='casDocument',
            new_name='document',
        ),
        migrations.AlterField(
            model_name='cas_summary',
            name='advisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
