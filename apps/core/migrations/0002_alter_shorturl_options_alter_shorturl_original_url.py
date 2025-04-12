# Generated by Django 4.2 on 2025-04-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shorturl',
            options={'ordering': ['-created'], 'verbose_name': 'сокращенная ссылка', 'verbose_name_plural': 'сокращенные ссылки'},
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.URLField(max_length=500, verbose_name='ссылка'),
        ),
    ]
