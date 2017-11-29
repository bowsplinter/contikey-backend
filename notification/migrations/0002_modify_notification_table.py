from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('user', '0001_create_user_table'),
      ('article', '0001_create_article_table'),
      ('notification', '0001_create_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE notification
            DROP COLUMN text,
            DROP COLUMN url,
            ADD COLUMN type VARCHAR(20),
            ADD COLUMN is_read BOOLEAN,
            ADD COLUMN article_id INT
        ;""",
        """
            ALTER TABLE notification
            DROP COLUMN type,
            DROP COLUMN article_id,
            DROP COLUMN is_read,
            ADD COLUMN text VARCHAR(500),
            ADD COLUMN url VARCHAR(500)
        """
        ),
        migrations.RunSQL("""
            ALTER TABLE notification
            ADD CONSTRAINT articleFK FOREIGN KEY(article_id) REFERENCES article(article_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;
        """,
        """
            ALTER TABLE notification
            DROP CONSTRAINT articleFK
        """
        )
    ]