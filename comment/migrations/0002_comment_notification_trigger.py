from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_create_comment_table'),
        ('notification', '0002_modify_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TRIGGER comment_notification AFTER INSERT ON comment
            FOR EACH ROW
            INSERT INTO notification (type, article_id, user_id, is_read)
            VALUES ('comment', NEW.article_id, NEW.user_id, false)
        """,
        "DROP TRIGGER comment_notification"
      )
    ]