# Generated by Django 4.2.5 on 2023-09-20 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='send_review',
            new_name='send',
        ),
    ]
