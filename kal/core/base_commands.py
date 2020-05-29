from cleo import Command as BaseCommand

from kal.libraries import shell


class Command(BaseCommand):
    def shell_call(self, command, output=None):
        return shell.call(command, output=output)
