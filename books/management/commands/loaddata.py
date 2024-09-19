from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import books from JSON.'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, required=False, help='Path to JSON file.')

    def handle(self, *args, **options):
        from books.management.commands.start_migrate_json import start_migrate_json
        start_migrate_json(options['file'])
