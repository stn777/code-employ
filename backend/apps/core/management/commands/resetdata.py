from django.core.management.base import BaseCommand, CommandError
from apps.core import test_data


class Command(BaseCommand):
    help = 'Resets all data in the database and reloads test data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-reload',
            action='store_true',
            dest='no-reload',
            default=False,
            help='Test data will NOT be reloaded'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(
            'WARNING: Executing this command will result in all data being cleaned from the database.'))
        confirm = input('Continue? (Y/N): ')
        while len(confirm) != 1 or confirm.lower() not in "yn":
            confirm = input('Please enter Y or N: ')
        try:
            if options['no-reload']:
                test_data.clear_data()
                self.stdout.write(self.style.SUCCESS(
                    'Successully cleared data.'))
            else:
                test_data.reset_data()
                self.stdout.write(self.style.SUCCESS(
                    'Successfully cleared data and reloaded test data.'))
        except Exception as e:
            raise CommandError(
                f'An error occured during execution: {e}')
