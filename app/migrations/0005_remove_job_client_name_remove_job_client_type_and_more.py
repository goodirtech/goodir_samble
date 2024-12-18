# Generated by Django 5.1.2 on 2024-10-31 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_client_status_alter_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='client_type',
        ),
        migrations.RemoveField(
            model_name='job',
            name='status',
        ),
        migrations.CreateModel(
            name='ClientJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('technician_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('job_description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=6)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='app.client')),
                ('job_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientJobs', to='app.jobcategory')),
                ('technician_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientJobs', to='app.technician')),
            ],
        ),
    ]
