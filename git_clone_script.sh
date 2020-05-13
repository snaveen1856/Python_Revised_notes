#!/bin/bash

touch /home/git_repo 2> /dev/null

if [ $? -eq 0 ]
then
  echo "Successfully created file"
  exit 0
else
  echo "Could not create file" >&2
  exit 1
fi
