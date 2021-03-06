# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_like_notification_trigger'),
        ('notification', '0004_modify_notification_table'),
    ]

    operations = [
        migrations.RunSQL(
            "DROP TRIGGER unsubscribe_channel",
            """
            CREATE TRIGGER unsubscribe_channel AFTER DELETE ON user_follows_channel
            FOR EACH ROW
            UPDATE channel SET num_subscribers = num_subscribers - 1 WHERE channel_id = OLD.channel_id;
            """
        ),
        migrations.RunSQL("""
            CREATE TRIGGER unfollow_notification AFTER DELETE ON user_follows_channel
            FOR EACH ROW
            DELETE FROM notification
            WHERE type = 'channel'
            AND type_id = OLD.channel_id
            AND channel_id = OLD.channel_id
            AND type_user_id = OLD.user_id
            AND user_id IN (
                SELECT user_id from channel WHERE channel_id = OLD.channel_id);
        """,
        "DROP TRIGGER unfollow_notification"
      )
    ]
