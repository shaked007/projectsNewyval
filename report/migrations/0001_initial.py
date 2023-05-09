# Generated by Django 4.0.3 on 2023-04-25 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitDate', models.CharField(blank=True, max_length=200)),
                ('submitter', models.CharField(max_length=100)),
                ('tkulim', models.JSONField(blank=True)),
                ('mahlaka', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('checkId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.check')),
            ],
        ),
    ]
