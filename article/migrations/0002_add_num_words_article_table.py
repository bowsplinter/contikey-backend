from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('article', '0001_create_article_table')
    ]

    operations = [
      migrations.RunSQL("""
        ALTER TABLE article
        ADD COLUMN num_words INT
        ;""",
        """
        ALTER TABLE article
        DROP COLUMN num_words
        """
      )
    ]