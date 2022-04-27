# DDNS
I have a chron job on a server that handles DDNS for a GoDaddy domain. 

It calls the file update_godaddy.sh which sets the environment variable for my sendgrid API key and runs the script update_godaddy.py.

Update go_daddy.py uses a GoDaddy API key and secret to access GoDaddy and check value of an A record to see if it matches the server's current WAN IP. 

If the IP doesn't match, the script updates the A record in GoDaddy and calls a function in joshtheadmin_email.py to notify me of the updated IP.  
