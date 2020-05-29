from cleo import argument, option

from kal.core.base_commands import Command
from kal.github import url_parsing


class CloneCommand(Command):
    name = 'clone'
    description = 'clone repository from github'
    arguments = [
        argument('repository', 'name of repository that you want to clone'),
        argument('target', 'target directory name', optional=True),
    ]
    options = [
        option('url', 'u', 'echo only url, not clone')
    ]

    def handle(self):
        clone_url = url_parsing(self.argument('repository'))
        if self.option('url'):
            self.line(clone_url)
            return 1
        command = 'git clone {}'.format(clone_url)
        if self.argument('target'):
            command += ' {}'.format(self.argument('target'))
        self.shell_call(command)
