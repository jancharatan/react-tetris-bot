#!/bin/sh

confirm() {
    read -p "[y/N] " response
    if [[ $response == "y" || $response == "Y" || $response == "yes" || $response == "Yes" ]]
    then
        return 0
    else 
        return 1
    fi
}

echo "Thanks for your interest in react-tetris-bot :)"

# Create venv
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip

# Install requirements + optionally dev requirements
printf "Do you want to install dev dependencies? 🤖 "
confirm && pip install -r requirements/dev.txt
pip install -r requirements/requirements.txt

echo "All done ✅"