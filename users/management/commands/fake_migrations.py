from django.core.management.base import BaseCommand
from django.db import connection
from django.db.migrations.recorder import MigrationRecorder

class Command(BaseCommand):
    help = 'Fakes the application of specific migrations.'

    def handle(self, *args, **options):
        migrations_to_fake = [
            ('users', '0009_buyer_lastname_buyer_points_buyer_updated_at'),
            ('users', '0010_buyer_points'),
            ('users', '0011_buyer_updated_at'),
        ]

        recorder = MigrationRecorder(connection)
        for app, migration in migrations_to_fake:
            self.stdout.write(f"Faking migration {app}.{migration}")
            recorder.record_applied(app, migration)

        self.stdout.write(self.style.SUCCESS('Successfully faked migrations.'))
