# Generated by Django 5.0.2 on 2024-02-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0002_rename_casdocument_cas_summary_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cas_summary',
            name='current_value',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]
