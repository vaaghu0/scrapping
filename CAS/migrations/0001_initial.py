# Generated by Django 5.0.2 on 2024-02-28 07:05

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cas_document',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'db_table': 'cas_documents',
            },
        ),
        migrations.CreateModel(
            name='cas_summary',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fund', models.TextField()),
                ('closing_balance', models.FloatField()),
                ('invested', models.FloatField()),
                ('allocation', models.FloatField()),
                ('folio', models.TextField(blank=True, null=True)),
                ('nav_date', models.DateField(blank=True, null=True)),
                ('advisor', models.TextField(blank=True, null=True)),
                ('casDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='cas.cas_document')),
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summaries',
                'db_table': 'cas_summary',
            },
        ),
    ]
