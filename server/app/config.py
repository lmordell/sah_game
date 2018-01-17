# app/config.py

""" Configuration settings for different builds """

###########
# Imports #
###########

from os.path import join, dirname
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

###########
# Classes #
###########

class BaseConfig(object):
    """Base configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing':     TestingConfig,
    'production':  ProductionConfig
}
