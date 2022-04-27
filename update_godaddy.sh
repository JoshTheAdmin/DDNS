echo "export SENDGRID_API_KEY='SENDGRID_APIKEY_HERE" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
python3 /home/ddns/update_godaddy.py