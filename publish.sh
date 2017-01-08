#!/bin/bash

suffix=$(pwd | tail -c4)
if [ "$suffix" == "com" ]; then
	suffix="com"
	locale="en_US"
elif [ "$suffix" == ".se" ]; then
	suffix="se"
	locale="sv_SE"
else
	exit
fi

echo $suffix
exit

git fetch --all
git reset --hard origin/gh-pages
echo "www.softwareyou.$suffix" > CNAME
git add CNAME
git commit CNAME -m "Add CNAME"
python3 l10n.py $locale
git add .
git commit -m "Run l10n"
git push --force
