# Generated by Django 5.0.4 on 2024-04-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onememos', '0002_alter_memo_tb_memo_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo_tb',
            name='writer_mail',
            field=models.CharField(default='xxxx@gmail.com', max_length=30),
        ),
        migrations.AddField(
            model_name='memo_tb',
            name='writer_nm',
            field=models.CharField(default='last-name + first-name', max_length=20),
        ),
    ]