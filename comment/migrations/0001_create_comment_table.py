# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('user', '0001_create_user_table'),
      ('article', '0001_create_article_table')
    ]

    operations = [
      migrations.RunSQL(
        """CREATE TABLE comment (
            comment_id INT AUTO_INCREMENT PRIMARY KEY,
            comment_text VARCHAR(500),
            user_id INT NOT NULL,
            article_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (article_id) REFERENCES article(article_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        "DROP TABLE comment"
      )
    ]
