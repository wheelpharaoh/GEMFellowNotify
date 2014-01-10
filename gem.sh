#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo "the dir is: $DIR"
if [ ! -f "$DIR"/gem.txt ]; then
   echo "file not found"
   python "$DIR"/gem3.py > "$DIR"/gem.txt
else
   #echo 'file found'
   diffresult="$(diff "$DIR"/gem.txt <(python "$DIR"/gem3.py))"
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
   echo "$diffresult" | mail -s "GEM update" EMAIL@DOMAIN.TLD
   python "$DIR"/gem3.py > "$DIR"/gem.txt
   fi
   #echo "finished diff"
fi