import pend

from kal.libraries.storage import Storage


class Note:
    note = None

    @classmethod
    def set_note(cls):
        cls.note = Storage.get('notes', {})

    @classmethod
    def keys(cls):
        if cls.note is None:
            cls.set_note()
        return cls.note.keys()

    @classmethod
    def value(cls, key):
        if cls.note is None:
            cls.set_note()
        return cls.note.get(key, {}).get('value')

    @classmethod
    def date(cls, key):
        if cls.note is None:
            cls.set_note()
        return cls.note.get(key, {}).get('date')

    @classmethod
    def set(cls, key, value):
        if cls.note is None:
            cls.set_note()
        cls.note[key] = {'value': value, 'date': pend.today().strftime('%Y-%m-%d %H:%M:%s')}
        return True

    @classmethod
    def delete(cls, key):
        if cls.note is None:
            cls.set_note()
        return cls.note.pop(key, None)

    @classmethod
    def save(cls):
        if cls.note is not None:
            Storage.set('notes', cls.note)
            Storage.save()
            return True
        else:
            return False
