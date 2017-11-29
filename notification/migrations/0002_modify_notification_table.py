from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('user', '0001_create_user_table'),
      ('notification', '0001_create_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE notification
            DROP COLUMN text
            DROP COLUMN url
            ADD COLUMN type VARCHAR(20)
            ADD COLUMN type_id INT NOT NULL
        """,
        """
            ALTER TABLE notification
            DROP COLUMN type
            DROP COLUMN type_id
            ADD COLUMN text VARCHAR(500)
            ADD COLUMN url VARCHAR(500)
        """
        )
    ]