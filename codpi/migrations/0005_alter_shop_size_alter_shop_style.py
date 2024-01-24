# Generated by Django 5.0.1 on 2024-01-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codpi', '0004_alter_shop_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='size',
            field=models.CharField(choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL'), ('xxxl', 'XXXL')], default='xl', max_length=6),
        ),
        migrations.AlterField(
            model_name='shop',
            name='style',
            field=models.CharField(choices=[('casual', 'Casual'), ('sports', 'Sports')], default='sports', max_length=25),
        ),
    ]