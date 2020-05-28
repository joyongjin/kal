import subprocess

from cleo import Command as BaseCommand


class Command(BaseCommand):
    def shell_call(self, command, output=None):
        if output is not None:
            output = getattr(subprocess, output.upper())

        return subprocess.run(command, shell=True, stdout=output, encoding='utf-8')
