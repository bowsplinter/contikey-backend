# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_init_entity_table'),
        ('tag', '0001_init_entity_table'),
    ]

    operations = [
      migrations.RunSQL(
        """CREATE TABLE channel_tags (
            channel_id INT NOT NULL,
            tag_id INT NOT NULL,
            PRIMARY KEY (channel_id, tag_id),
            FOREIGN KEY (channel_id) REFERENCES channel(channel_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );""",
        "DROP TABLE channel_tags"
      )
    ]
