#! /bin/sh
echo "********************"
echo "Welcome to my app "

if [ -d "env" ];
then
    echo "env exists"
else
    echo "creating Virtualenv"
    python3.10 -m venv env
fi

. env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

deactivate

echo " Now run local_setup.sh to run the server "
