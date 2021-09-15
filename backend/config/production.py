# import os

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from .common import Common


class Production(Common):
    # pass
    INSTALLED_APPS = Common.INSTALLED_APPS
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["production.hostname.com"]

    # sentry_sdk.init(
    #     dsn=os.getenv('DJANGO_SENTRY_DSN_URL'),
    #     integrations=[DjangoIntegration()]
    # )
