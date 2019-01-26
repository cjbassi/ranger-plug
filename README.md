# ranger-plug

Small python script to manage [Ranger](https://github.com/ranger/ranger) plugins.

Install with

```bash
pip install --user git+https://github.com/cjbassi/ranger-plug
```

Subcommands include:

- `install [repos]`
- `uninstall [repos]`
- `update`

Repos have the following format with host and branch optional:

```
{host}/{owner}/{name}@{branch}  : github.com/cjbassi/ranger-plug@master
```
