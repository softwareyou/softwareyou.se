Software & You Website

This is the template for the Software & You website.
It contains all resources required to build softwareyou.se and softwareyou.com.

Instructions:

Make changes in this repository and push to remote.
Switch to the softwareyou.{se|com} repository.

1. `git fetch --all`
1. `git reset --hard`
1. `python l10n {sv_SE|en_US}`
1. `git commit -m "l10n {sv_SE|en_US}"`
1. `git push`

Prerequisite:

```
$ git remote -v
origin  git@github.com:softwareyou/softwareyou.git (fetch)
origin  git@github.com:softwareyou/softwareyou.com.git (push)
```