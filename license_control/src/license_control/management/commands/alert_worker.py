# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from license_control.tasks import SendMailTasks


class Command(BaseCommand):
    help = 'Start alert worker'

    def handle(self, *args, **options):
        self.stdout.write('Starting Alert Worker...')
        consumer = SendMailTasks()
        try:
            self.stdout.write('Alert worker is running...')
            consumer.run()
        except KeyboardInterrupt:
            self.stdout.write('Stopping Alert Worker...')
