# Generated by Django 5.0.7 on 2024-08-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
