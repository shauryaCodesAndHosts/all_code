#! /bin/sh
echo "start virtualenv"
if [ -d "env" ];
then
    echo "enabling virtual env"
else
    echo "run setup.sh first"
    exit N
fi

. env/bin/activate
export ENV=development
python main.py
deactivate