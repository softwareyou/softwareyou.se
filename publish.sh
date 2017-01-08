#!/bin/bash
if [ "$#" -ne 2 ]; then
	echo "'./publish se sv_SE'" or "'./publish com en_US'"
	exit
fi

git fetch --all
git reset --hard origin/gh-pages
echo "www.softwareyou.$1" > CNAME
git add CNAME
git commit CNAME -m "Add CNAME"
python3 l10n.py $2
git add .
git commit -m "Run l10n"
git push --force
