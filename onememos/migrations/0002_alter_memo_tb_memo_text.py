# Generated by Django 5.0.4 on 2024-04-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onememos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo_tb',
            name='memo_text',
            field=models.CharField(max_length=250),
        ),
    ]