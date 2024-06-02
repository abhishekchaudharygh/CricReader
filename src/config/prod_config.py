from .base_config import BaseConfig


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False
    DEBUG = True