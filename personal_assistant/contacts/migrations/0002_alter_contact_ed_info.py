# Generated by Django 5.1 on 2024-08-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ed_info',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]