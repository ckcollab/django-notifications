# Generated by Django 5.0.2 on 2024-02-15 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0009_alter_notification_options_and_more"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="notification",
            new_name="notificatio_recipie_8bedf2_idx",
            old_fields=("recipient", "unread"),
        ),
    ]
