# Generated by Django 4.1.5 on 2023-01-19 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_usermodel_confirmpassword_alter_usermodel_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='fullname',
            new_name='username',
        ),
    ]
