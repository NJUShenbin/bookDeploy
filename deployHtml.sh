#!/bin/bash
cd "$1"
git pull origin
gitbook install
gitbook build
rm -r /var/www/html/book
cp -r ./_book /var/www/html/book
