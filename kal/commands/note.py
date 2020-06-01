from cleo import option, argument

from kal.core.base_commands import Command
from kal.libraries.note import Note


class NoteCommand(Command):
    name = 'note'
    description = 'note command'
    arguments = [
        argument('key', 'key of note item', optional=True),
        argument('value', 'value if you want to save or overwrite key.', optional=True),

    ]
    options = [
        option('delete', 'd', 'delete key note'),
        option('list', 'l', 'list of notes'),
    ]

    def handle(self):
        key = self.argument('key')
        value = self.argument('value')
        if self.option('list'):
            if key is None:
                keys = Note.keys()
                if len(keys) == 0:
                    self.line_error('Empty notebook')
                    return 0
                for k in keys:
                    self.line('{} {}'.format(Note.date(k), k))
                return 0
            else:
                self.line_error('list option do not need key')
                return 1
        elif key is None:
            self.line_error('Missing required argument: key')
            return 1

        if self.option('delete'):
            if value is None:
                result = Note.delete(key)
                if result is None:
                    self.line_error('{} is not in notebook'.format(key))
                    return 0
                else:
                    Note.save()
                    self.line('{} was deleted'.format(key))
                    return 0
            else:
                self.line_error('delete option do not need value')
                return 1

        if value is None:
            self.line(Note.value(key) or '')
            return 0

        Note.set(key, value)
        Note.save()
