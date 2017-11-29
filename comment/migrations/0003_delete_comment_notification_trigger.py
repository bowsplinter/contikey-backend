from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_create_comment_table'),
        ('comment', '0002_comment_notification_trigger'),
        ('notification', '0002_modify_notification_table')
    ]

    operations = [
        migrations.RunSQL(
        "DROP TRIGGER comment_notification",
        """
            CREATE TRIGGER comment_notification AFTER INSERT ON comment
            FOR EACH ROW
            INSERT INTO notification (type, article_id, user_id, is_read, type_user_id)
            VALUES ('comment', NEW.article_id, (
                 SELECT user_id from channel WHERE channel_id IN (
-                    SELECT channel_id FROM article WHERE article_id = NEW.article_id)))
+                    SELECT channel_id FROM article WHERE article_id = NEW.article_id)), false, NEW.user_id)
        """
      )
    ]