import json

from kal.env import path


class BaseJson:
    filepath = None
    default_data = {}
    data = None

    @classmethod
    def get_default_data(cls):
        return cls.default_data

    @classmethod
    def initialize(cls):
        if not path.exists(cls.filepath):
            with open(cls.filepath, 'w') as f:
                json.dump(cls.get_default_data(), f)
        with open(path.STORAGE_FILE, 'r') as f:
            cls.data = json.load(f)

    @classmethod
    def get(cls, key, default=None):
        return cls.data.get(key, default=default)


class WritableJson(BaseJson):
    @classmethod
    def set(cls, key, value):
        cls.data[key] = value
        return value

    @classmethod
    def bulk_set(cls, **kwargs):
        for key, value in kwargs.items():
            cls.set(key, value)
        return True

    @classmethod
    def delete(cls, key):
        return cls.data.pop(key, None)

    @classmethod
    def save(cls):
        with open(cls.filepath, 'w') as f:
            json.dump(cls.data, f)
