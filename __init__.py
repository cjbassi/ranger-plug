import shutil
import os

from ranger.api.commands import Command

from xdg import XDG_DATA_HOME, XDG_CONFIG_HOME
import git

PLUGINS_PATH = os.path.join(XDG_DATA_HOME, 'ranger', 'plugins')
CONFIG_FILE = os.path.join(XDG_CONFIG_HOME, 'ranger', 'plugin_list')
PLUGIN_NAME = "ranger-plug"


class Repo:
    def __init__(self, host, owner, name, branch):
        self.host = host
        self.owner = owner
        self.name = name
        self.branch = branch

    def __str__(self):
        if self.branch == "master":
            return self.url
        else:
            return self.url + "@" + self.branch

    @property
    def url(self):
        return "https://{}/{}/{}".format(self.host, self.owner, self.name)


def get_repos_list():
    repos = []
    with open(CONFIG_FILE, 'r') as f:
        for line in f:
            line = line.strip()

            fields = line.split('@')
            branch = fields[1] if len(fields) == 2 else "master"

            fields = fields[0].split('/')
            name = fields[-1]
            owner = fields[-2]
            host = fields[0] if len(fields) == 3 else "github.com"

            repos.append(Repo(host, owner, name, branch))

    return repos


class PlugInstall(Command):
    def execute(self):
        repos = get_repos_list()
        for repo in repos:
            path = os.path.join(PLUGINS_PATH, repo.name)
            if not os.path.exists(path):
                # print("Cloning {}".format(repo))
                git.Git(PLUGINS_PATH).clone(repo.url)
                git.Repo(path).git.checkout(repo.branch)


class PlugUpdate(Command):
    def execute(self):
        for name in os.listdir(PLUGINS_PATH):
            path = os.path.join(PLUGINS_PATH, name)
            git.Repo(path).git.pull()


class PlugClean(Command):
    def execute(self):
        repo_names = list(map(lambda repo: repo.name, get_repos_list()))
        for name in os.listdir(PLUGINS_PATH):
            if name not in repo_names and name != PLUGIN_NAME:
                # print("Removing {}".format(name))
                path = os.path.join(PLUGINS_PATH, name)
                shutil.rmtree(path)
