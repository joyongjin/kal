import json

from kal.env import path
from kal.utils import dig

with open(path.CONFIG_FILE) as f:
    config_json = json.load(f)


def config_get(*keys, default=None):
    return dig(config_json, *keys, default=default)
