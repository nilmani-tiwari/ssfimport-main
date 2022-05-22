from django.apps import AppConfig


class PaypalPaymentConfig(AppConfig):
    name = 'paypal_payment'

    def ready(self):
        from . import updater
        updater.start()
