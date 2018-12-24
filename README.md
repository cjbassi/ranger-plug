# ranger-plug

Install with

```bash
git clone https://github.com/cjbassi/ranger-plug ~/.local/share/ranger/plugins/ranger-plug
pip install --user xdg gitpython
```

Commands include:

- PlugInstall
- PlugUpdate
- PlugClean

Specify git repos to install in a `~/.config/ranger/plugin_list` file.
Repos can have the following format:

```
{host}/{owner}/{name}@{branch}  : github.com/cjbassi/ranger-plug@master
{owner}/{name}@{branch}         : cjbassi/ranger-plug@master (github.com assumed)
{owner}/{name}                  : cjbassi/ranger-plug
```
