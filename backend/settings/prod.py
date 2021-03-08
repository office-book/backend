import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['https://officebook-backend-staging.herokuapp.com/']

DATABASES = os.environ['DATABASE_URL']
