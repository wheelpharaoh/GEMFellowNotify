#!/bin/bash
if [ ! -f `pwd`/gem.txt ]; then
   echo "file not found"
   python `pwd`/gem3.py > `pwd`/gem.txt
else
   #echo 'file found'
   diffresult="$(diff `pwd`/gem.txt <(python `pwd`/gem3.py))"
   #echo $diffresult
   if [ ! -z "$diffresult" ]; then
      #echo "GEM: new update!"
      subject="GEM update"
      URL="https://api.pushover.net/1/messages.json"
      API_KEY=""
      USER_KEY=""
      TITLE=$subject
      MESSAGE="$diffresult"
      `which curl` \
	-F "token=${API_KEY}" \
	-F "user=${USER_KEY}" \
	-F "title=${TITLE}" \
	-F "message=${MESSAGE}" \
       "${URL}" > /dev/null 2>&1
   fi
   #echo "finished diff"
fi
