from kal.core.json_obj import BaseJson
from kal.env import path
from kal.utils import dig


class Config(BaseJson):
    filepath = path.CONFIG_FILE
    default_data = {
        "github": {
            "username": "joyongjin"
        },
        "storage": {
            "default": {}
        }
    }

    @classmethod
    def get(cls, *keys, default=None):
        return dig(cls.data, *keys, default=default)
