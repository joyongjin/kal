from cleo import argument

from kal.github import url_parsing
from .base import Command


class CloneCommand(Command):
    name = 'clone'
    description = 'clone repository from github'
    arguments = [
        argument('repository', 'name of repository that you want to clone'),
        argument('target', 'target directory name', optional=True),
    ]

    def handle(self):
        clone_url = url_parsing(self.argument('repository'))
        command = 'git clone {}'.format(clone_url)
        if self.argument('target'):
            command += ' {}'.format(self.argument('target'))
        self.shell_call(command)
