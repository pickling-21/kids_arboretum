#!/bin/bash
set -e

echo -e "\e[0;92m[INFO]\e[0m Checking files...\n"


if grep -q token squads/secret.py; then 
    echo ""
else
    if [ -z "$1" ]; then 
        echo -e "\033[0;91m[ERROR]\033[0m Need token to continue. Please try: deploy.sh TOKEN\n"
        exit
    fi
    touch squads/secret.py
    echo -e "token = \"$1\"" >> squads/secret.py
fi

echo -e "\e[0;92m[INFO]\e[0m Installing dependencies ...\n"

sudo apt-get install python3-pip -y
pip3 install -r requirements.txt

echo -e "\n\e[0;92m[INFO]\e[0m Running bot ...\n"


python3 main.py 