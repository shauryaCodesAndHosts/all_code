#! /bin/sh
echo "start virtualenv"
if [ -d "env" ];
then
    echo "enabling virtual env"
else
    echo "run setup.sh first"
    exit 
fi
. env/bin/activate
export ENV=development
python app.py
deactivate