#!/usr/bin/env bash

#add all the files
git add -A

#commit with a defult message
echo "Commit message: $1"
git commit -m "$1"

#push 
git push origin master
