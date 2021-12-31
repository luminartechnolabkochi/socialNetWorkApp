# Generated by Django 4.0 on 2021-12-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('accepted', 'Accepted')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender'), ('others', 'Others')], max_length=100, null=True),
        ),
    ]
