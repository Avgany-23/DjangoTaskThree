from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import phones from CSV.'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, required=False, help='Path to CSV file.')

    def handle(self, *args, **options):
        from phones.management.commands.import_phones import start_migrate_csv
        start_migrate_csv(options['file'])
