from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_modify_user_attributes'),
        ('notification', '0003_add_type_user_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TRIGGER like_notification AFTER INSERT ON user_likes_article
            FOR EACH ROW
            INSERT INTO notification (type, type_id, article_id, user_id, is_read, type_user_id)
            VALUES ('like', NEW.article_id, NEW.article_id, (
                 SELECT user_id from channel WHERE channel_id IN (
                     SELECT channel_id FROM article WHERE article_id = NEW.article_id)), false, NEW.user_id);
        """,
        "DROP TRIGGER like_notification"
      )
    ]