from cleo import argument
from cleo.commands.base_command import CommandError

from kal.core.base_commands import Command
from kal.env import path

"""
link # link all ln script

"""

LINK_PATH = {
    'ssh': ('keys/.ssh', '$HOME/'),
    'vimrc': ('settings/.vimrc', '$HOME/'),
    'zshrc': ('settings/zsh/.zshrc_ubuntu', '$HOME/.zshrc'),
    'pypirc': ('settings/.pypirc', '$HOME/'),
    'aws': ('keys/.aws', '$HOME/'),
    'terminator': ('settings/terminator', '$HOME/.config/'),
}


class BoxCommand(Command):
    name = 'box'
    description = 'Dropbox helper command'
    arguments = [
        argument('command'),
        argument('args', multiple=True)
    ]

    def check_args(self, length):
        args = self.argument('args')
        if len(args) < length:
            raise CommandError('Invalid length of arguments: {}'.format(args))
        return args

    def handle(self):
        command = self.argument('command')
        if command == 'link':
            args = self.check_args(1)
            self.link(args[0])
        else:
            raise CommandError('Invalid command')

    def link(self, name):
        link_path = LINK_PATH.get(name)
        sc = 'ln -sf {} {}'.format(
            path.join(path.DROPBOX_DIR, link_path[0]),
            link_path[1],
        )
        self.shell_call(sc)
