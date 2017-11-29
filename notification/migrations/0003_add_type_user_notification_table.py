from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('user', '0001_create_user_table'),
      ('article', '0001_create_article_table'),
      ('notification', '0001_create_notification_table'),
      ('notification', '0002_modify_notification_table')
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE notification
            ADD COLUMN type_user_id INT
        ;""",
        """
            ALTER TABLE notification
            DROP COLUMN type_user_id
        """
        ),
        migrations.RunSQL("""
            ALTER TABLE notification
            ADD CONSTRAINT type_userFK FOREIGN KEY(type_user_id) REFERENCES user(user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;
        """,
        """
            ALTER TABLE notification
            DROP FOREIGN KEY type_userFK;
        """
        )
    ]