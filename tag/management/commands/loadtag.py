from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from tag.sql import add_tag, delete_all_tags
import json

class Command(BaseCommand):
    help = 'Populates tag table with tag data'

    def add_arguments(self, parser):
        parser.add_argument('data_path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['data_path'][0]
        with open(path) as file:
            tags = json.loads(file.read())
        delete_all_tags()
        for tag in tags:
            add_tag(tag['fields'])