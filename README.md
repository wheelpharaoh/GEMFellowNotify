GEMFellowNotify
===============

scrape GEM Fellowship applicant account page and send pushover notif 

dependencies:
curl
python 2.7
- lxml
- configparser
- mechanize

setup:
$ vi gem.ini
[account]
email=username@domain.com
password=passwd

$ vi gem.sh
API_KEY=pushover API key
USER_KEY=pushover User key

chmod +x gem3.py gem.sh

first run:
python gem3.py > ./gem.txt

usage:
bash gem.sh

cron:
$ crontab -e
* * * * * root gem.sh
