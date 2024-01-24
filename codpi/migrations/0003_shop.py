# Generated by Django 5.0.1 on 2024-01-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codpi', '0002_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=80)),
                ('size', models.CharField(max_length=6)),
                ('color', models.CharField(default='pink', max_length=15)),
                ('style', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='cloth/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]