from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_like_notification_trigger'),
        ('notification', '0003_add_type_user_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TRIGGER follow_notification AFTER INSERT ON user_follows_channel
            FOR EACH ROW
            INSERT INTO notification (type, type_id, channel_id, user_id, is_read, type_user_id)
            VALUES ('channel', NEW.channel_id, NEW.channel_id, (
                 SELECT user_id from channel WHERE channel_id = NEW.channel_id), false, NEW.user_id);
        """,
        "DROP TRIGGER follow_notification"
      )
    ]