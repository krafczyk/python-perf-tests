set -e

if [ ! -e venv ]; then
    virtualenv venv
fi;

source venv/bin/activate
