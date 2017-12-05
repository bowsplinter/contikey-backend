from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_unsubscribe_channel_trigger'),
        ('notification', '0004_modify_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TRIGGER delete_like_notification AFTER DELETE ON user_likes_article
            FOR EACH ROW
            DELETE FROM notification
            WHERE
                type = 'like'
            AND type_id = OLD.article_id
            AND article_id = OLD.article_id
            AND type_user_id = OLD.user_id
            AND user_id IN (
                SELECT user_id from channel WHERE channel_id IN (
                     SELECT channel_id FROM article WHERE article_id = OLD.article_id))
        """,
        "DROP TRIGGER delete_like_notification"
      )
    ]