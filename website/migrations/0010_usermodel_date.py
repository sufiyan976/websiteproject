# Generated by Django 4.1.5 on 2023-01-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_usermodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
