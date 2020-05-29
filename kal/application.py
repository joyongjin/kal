from cleo import Application as BaseApplication

from kal import __version__
from kal.initialize import init
from .commands import CloneCommand
from .commands.time import KSTCommand, UTCCommand


class Application(BaseApplication):
    def __init__(self, *args, **kwargs):
        init()
        super().__init__('kal', __version__)
        for command in self.get_default_commands():
            self.add(command)

    def get_default_commands(self):
        commands = [
            CloneCommand(),
            KSTCommand(),
            UTCCommand(),
        ]
        return commands
