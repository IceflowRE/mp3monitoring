#!/bin/sh
# executed from project root

app_version=$(grep -oP "VERSION\s=\s'\K\w+.\w+.\w+" ./mp3monitoring/data/static.py)
rls_date=`date +%Y-%m-%d`

# change online version for updater
echo -e "$app_version""\c" > ./version

# change versions in installer
version_regex="[a-zA-Z0-9]\+\.[a-zA-Z0-9]\+\.[a-zA-Z0-9]\+"
sed -i 's/<Version>'"$version_regex"'<\/Version>/<Version>'"$app_version"'<\/Version>/' ./installer/hybrid/config/config.xml
sed -i 's/<Version>'"$version_regex"'<\/Version>/<Version>'"$app_version"'<\/Version>/' ./installer/hybrid/packages/mp3monitoring/meta/package.xml
sed -i 's/<Version>'"$version_regex"'<\/Version>/<Version>'"$app_version"'<\/Version>/' ./installer/hybrid/packages/mp3monitoring.gui/meta/package.xml
sed -i 's/<Version>'"$version_regex"'<\/Version>/<Version>'"$app_version"'<\/Version>/' ./installer/hybrid/packages/mp3monitoring.updater/meta/package.xml

# change release date
sed -i 's/<ReleaseDate>[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}<\/ReleaseDate>/<ReleaseDate>'"$rls_date"'<\/ReleaseDate>/' ./installer/hybrid/packages/mp3monitoring/meta/package.xml
sed -i 's/<ReleaseDate>[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}<\/ReleaseDate>/<ReleaseDate>'"$rls_date"'<\/ReleaseDate>/' ./installer/hybrid/packages/mp3monitoring.gui/meta/package.xml
sed -i 's/<ReleaseDate>[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}<\/ReleaseDate>/<ReleaseDate>'"$rls_date"'<\/ReleaseDate>/' ./installer/hybrid/packages/mp3monitoring.updater/meta/package.xml
