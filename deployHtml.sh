#!/bin/bash

#$1 gitUrl
#$2 repoName (by caller splite from gitUrl)
#$3 deploy dir (such as "mybook",will be deployed to /var/www/html/mybook)
gitUrl=$1
repoName=$2
deployDir=$3

echo "--------start build--------"
curday=`date '+%Y-%m-%d %H:%M:%S'`
echo $curday

#goto current shell file dir
cd `dirname $0`
#goto local books dir
cd ./localGitbook

if [ ! -d $repoName ]; then
    git clone $gitUrl.git
    cd ./$repoName
else
    cd ./$repoName
    git pull origin
fi

gitbook install
gitbook build
rm -r /var/www/html/$deployDir
cp -r ./_book /var/www/html/$deployDir
echo "---------end build---------"