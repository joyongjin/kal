import os


class path:
    @staticmethod
    def join(*args, **kwargs):
        return os.path.join(*args, **kwargs)

    @staticmethod
    def exists(p):
        return os.path.exists(p)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BASE_DIR)

    if os.getenv('KAL_HOME_PATH'):
        HOME_DIR = os.getenv('KAL_HOME_PATH')
    else:
        HOME_DIR = os.path.join(os.getenv('HOME'), '.kal')

    CONFIG_FILE = os.path.join(HOME_DIR, 'config.json')
    STORAGE_FILE = os.path.join(HOME_DIR, 'storage.json')
