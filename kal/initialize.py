import os

from kal.libraries.config import Config
from kal.env import path
from kal.libraries.storage import Storage


def init():
    if not path.exists(path.HOME_DIR):
        os.makedirs(path.HOME_DIR, exist_ok=True)
    Config.initialize()
    Storage.initialize()
