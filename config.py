import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    PROPAGATE_EXCEPTIONS = True
    THREADED = True
    # INFO: temporary code while login app is being used here.
    # PREFERRED_URL_SCHEME = 'https'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = 5000 if os.environ.get("PORT") is None else int(os.environ.get("PORT"))
    HOST = os.environ.get('HOST') or 'localhost'
    PREFERRED_URL_SCHEME = 'http'


class QaConfig(BaseConfig):
    DEBUG = False
    PORT = 8080 if os.environ.get("PORT") is None else int(os.environ.get('PORT'))
    HOST = os.environ.get('HOST') or '0.0.0.0'


class ProductionConfig(BaseConfig):
    DEBUG = False
    PORT = 8080 if os.environ.get("PORT") is None else int(os.environ.get('PORT'))
    HOST = os.environ.get('HOST') or '0.0.0.0'
