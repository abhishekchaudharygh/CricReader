from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True