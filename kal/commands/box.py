from cleo import argument
from cleo.commands.base_command import CommandError

from kal.core.base_commands import Command
from kal.env import path

"""
link # link all ln script
git # git settings
"""

LINK_PATH = {
    'ssh': ('keys/.ssh', '$HOME/'),
    'vimrc': ('settings/.vimrc', '$HOME/'),
    'zshrc': ('settings/zsh/.zshrc_ubuntu', '$HOME/.zshrc'),
    'pypirc': ('settings/.pypirc', '$HOME/'),
    'aws': ('keys/.aws', '$HOME/'),
    'terminator': ('settings/terminator', '$HOME/.config/'),
}

GIT_SETTINGS_COMMANDS = """
git config --global alias.co commit
git config --global alias.ad add
git config --global alias.aa 'add --all'
git config --global alias.cf config
git config --global alias.cm 'commit -m'
git config --global alias.ss 'status --short'
git config --global alias.s status
git config --global alias.st stash
git config --global alias.rs reset
git config --global alias.rb rebase
git config --global alias.last 'log -1 HEAD'
git config --global alias.rt remote
git config --global alias.us 'reset HEAD --'
git config --global alias.ca 'commit --amend'
git config --global alias.adog 'log --all --oneline --decorate --graph'
git config --global core.excludesfile ~/Dropbox/settings/.gitignore_global/.gitignore_global
git config --global alias.ch checkout
git config --global alias.br branch
git config --global core.editor vim
git config --global user.email 'wnrhd114@gmail.com'
git config --global user.name 'joyongjin'
git config --global color.ui true
""".strip().split("\n")


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
        if command == 'git':
            self.check_args(0)
            self.git()
        else:
            raise CommandError('Invalid command')

    def link(self, name):
        link_path = LINK_PATH.get(name)
        sc = 'ln -sf {} {}'.format(
            path.join(path.DROPBOX_DIR, link_path[0]),
            link_path[1],
        )
        self.shell_call(sc)

    def git(self):
        for c in GIT_SETTINGS_COMMANDS:
            self.shell_call(c)
