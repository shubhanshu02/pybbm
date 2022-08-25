# coding=utf-8

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PybbConfig(AppConfig):
    name = "pybb"
    verbose_name = _("Pybbm forum solution")

    def ready(self):
        from pybb import signals

        signals.setup()
