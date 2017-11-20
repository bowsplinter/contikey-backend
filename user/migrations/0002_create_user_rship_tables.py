# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
      ('user', '0001_create_user_table'),
      ('tag', '0001_create_tag_table'),
      ('channel', '0001_create_channel_table'),
      ('article', '0001_create_article_table'),
    ]

    operations = [
      migrations.RunSQL(
        """CREATE TABLE user_friends (
            user_id INT,
            friend_id INT,
            PRIMARY KEY (user_id, friend_id),
            FOREIGN KEY (user_id) REFERENCES user(user_id)
                ON DELETE CASCADE,
            FOREIGN KEY (friend_id) REFERENCES user(user_id)
                ON DELETE CASCADE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        "DROP TABLE user_friends"
      ),
      migrations.RunSQL(
        """CREATE TABLE user_follows_tag (
            user_id INT NOT NULL,
            tag_id INT NOT NULL,
            PRIMARY KEY (user_id, tag_id),
            FOREIGN KEY (user_id) REFERENCES user(user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );""",
        "DROP TABLE user_follows_tag"
      ),
      migrations.RunSQL(
        """CREATE TABLE user_follows_channel (
            user_id INT NOT NULL,
            channel_id INT NOT NULL,
            PRIMARY KEY(user_id, channel_id),
            FOREIGN KEY (user_id) REFERENCES user(user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (channel_id) REFERENCES channel(channel_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        "DROP TABLE user_follows_channel"
      ),
      migrations.RunSQL(
        """CREATE TABLE user_likes_article (
            user_id INT NOT NULL,
            article_id INT NOT NULL,
            likeStatus TINYINT CHECK(likeStatus=1 OR likeStatus=-1),
            PRIMARY KEY (user_id, article_id),
            FOREIGN KEY (user_id) REFERENCES user(user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (article_id) REFERENCES article(article_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            created_at TIMESTAMP
        );""",
        "DROP TABLE user_likes_article"
      )
    ]