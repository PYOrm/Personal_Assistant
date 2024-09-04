# Generated by Django 5.1.1 on 2024-09-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120)),
                ('box_file_id', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('image', 'Image'), ('document', 'Document'), ('video', 'Video'), ('other', 'Other')], max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
