# Generated by Django 4.1.7 on 2023-11-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popfeed', '0002_alter_commentlikes_options_alter_poplikes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]