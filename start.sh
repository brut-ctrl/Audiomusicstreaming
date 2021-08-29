echo "Cloning Repo...."
git clone https://github.com/brut-ctrl/Audiomusicstreaming.git /Audiomusicstreaming
cd /Audiomusicstreaming
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py