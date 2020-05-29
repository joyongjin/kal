from kal.config import Config
from kal.core.json_obj import WritableJson
from kal.env import path


class Storage(WritableJson):
    filepath = path.STORAGE_FILE

    @classmethod
    def get_default_data(cls):
        default_data = cls.default_data
        default_data.update(Config.get('storage', 'default', default=dict()))
        return default_data
