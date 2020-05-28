import json


class JsonObject:
    default_data = {}

    def __init__(self):
        self.data = self.default_data
        self.data.update(**self.load_json())

    def get_filename(self):
        return ''

    def load_json(self, filename=None):
        if filename is None:
            filename = self.get_filename()
        with open(filename, 'r') as f:
            loaded_data = json.load(f)
        return loaded_data

    def write_json(self, data, filename=None):
        if filename is None:
            filename = self.get_filename()

        with open(filename, 'w') as f:
            json.dump(data, f)
        return True

    def get(self, key, default=None):
        return self.data.get(key, default=default)

    def set(self, key, value):
        self.data[key] = value
        return value

    def save(self):
        self.write_json(self.data)
        return True
