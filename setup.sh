set -e

echo "1"
if [ ! -e venv ]; then
    virtualenv venv
fi;

echo "2"
source venv/bin/activate
echo "3"
pip install -r requirements.txt
