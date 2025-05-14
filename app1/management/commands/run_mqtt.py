from django.core.management.base import BaseCommand
from app1.pahomqtt import mqtt_connect  # Make sure this matches your actual file

class Command(BaseCommand):
    help = 'Starts the MQTT subscriber'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting MQTT Subscriber..."))
        mqtt_connect()
