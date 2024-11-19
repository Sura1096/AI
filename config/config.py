import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.env'))


class ApiSettings:
    AUTH_KEY: str = os.environ.get('AUTH_KEY')

api_settings = ApiSettings()
