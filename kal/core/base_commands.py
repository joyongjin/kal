import pend
from cleo import Command as BaseCommand

from kal.libraries import shell


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.cwd = None

    def before_handle(self):
        pass

    def after_handle(self, response):
        return response

    def wrap_handle(self, *args, **kwargs):
        self.before_handle()
        response = super().wrap_handle(*args, **kwargs)
        response = self.after_handle(response)
        return response

    def shell_call(self, command, output=None, **kwargs):
        if self.cwd is not None and 'cwd' not in kwargs:
            kwargs['cwd'] = self.cwd
        return shell.call(command, output=output, **kwargs)

    def line_error(self, text, style='error', verbosity=None):
        return super().line_error(text, style=style, verbosity=verbosity)


class TimeCommand(Command):
    mapper = ['hour', 'minute', 'second']

    def time_parse(self, time=None, from_tz='KST', target_tz=None):
        if time is None:
            time = self.argument('time')
        if target_tz is None:
            target_tz = self.argument('target_tz')

        time_arr = time.split(':')

        today = pend.today(from_tz)
        for index, v in enumerate(time_arr):
            today = today.replace(**{self.mapper[index]: int(v)})

        return today.in_timezone(target_tz)
