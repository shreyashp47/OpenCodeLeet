import os

APP_NAME = "OpenCodeLeet"
APP_VERSION = "2.0.0"
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
EXECUTION_TIMEOUT = 3.0
