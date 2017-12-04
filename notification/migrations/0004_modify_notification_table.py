from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('channel', '0002_create_channel_tag_tables'),
      ('notification', '0003_add_type_user_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE notification
            ADD COLUMN type_id INT,
            ADD COLUMN channel_id INT
        ;""",
        """
            ALTER TABLE notification
            DROP COLUMN channel_id INT,
            DROP COLUMN type_id
        """
        ),
        migrations.RunSQL("""
            ALTER TABLE notification
            ADD CONSTRAINT channelFK FOREIGN KEY(channel_id) REFERENCES channel(channel_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;
        """,
        """
            ALTER TABLE notification
            DROP FOREIGN KEY channelFK;
        """
        )
    ]