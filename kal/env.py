import os


class path:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)
    CONFIG_FILE = os.path.join(PROJECT_DIR, 'config.json')
