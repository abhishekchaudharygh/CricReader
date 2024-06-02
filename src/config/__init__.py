import os
from dotenv import load_dotenv
from .dev_config import DevelopmentConfig
from .prod_config import ProductionConfig

ROOT_DIR = os.path.join(os.path.dirname(__file__), "../..")
DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")

load_dotenv(DOT_ENV_PATH)

config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}


def init_app(app):
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(config[app_settings])
    return app
