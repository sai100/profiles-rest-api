# Generated by Django 3.2.16 on 2023-01-02 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileFeed',
            new_name='ProfileFeedItem',
        ),
    ]
