#!/usr/bin/env python

# Import pif to get your public ip, sys and os.path
import pif, sys, os.path, smtplib, ssl
from joshtheadmin_email import ipupdate_notification

# Partial imports
from godaddypy import Client, Account

# Remember to set your api key and secret
userAccount = Account(api_key='GODADDY_API_KEY', api_secret='GODADDY_API_SECRET')
userClient = Client(userAccount)
publicIP = pif.get_public_ip('ident.me')

# E.g.: to update your_record.yourdomain.com set domain and record to:
domain = 'domain_to_update'
a_record = 'record_to_update'

#The following attribute is a "note" field. I have a NAT rule I need to update on my roommate's
#Verizon router so I have added this note to my email
notes = "Please update the NAT rule on the Verizon router"

"""
if os.path.isfile('godaddy_ip.txt'):
    try:
        ip_file = open('godaddy_ip.txt', 'r')
        read_ip = ip_file.read().strip('\n')
        ip_file.close()
    except:
        print("Cannot read IP file")
        sys.exit()
    if read_ip == publicIP:
        print("Read the IP file, no need to change IP")
        sys.exit()
"""

# Try to retrieve the record and update it if necessary 
try:
    currentIP = userClient.get_records(domain, record_type='A', name=a_record)
    if (publicIP != currentIP[0]["data"]):
        updateResult = userClient.update_record_ip(publicIP, domain, a_record, 'A')
        if updateResult is True:
            ip_file = open('godaddy_ip.txt', 'w')
            ip_file.write(publicIP)
            ip_file.close()
            print('Updated DNS record and wrote IP file.')
            ipupdate_notification((a_record + '.' + domain),publicIP, 'jwallace@joshtheadmin.com',notes)  
# I have this set to email a notification to jwallace@joshtheadmin.com, but you will want to put your email there. 
# You will need to update the SPF record for your domain if you want to avoid spam filters. 
# This script could be adpated to also update the SPF record as the IP changes.           
    else:
        print('Checked the DNS record, no update needed.')
except:
    print(sys.exc_info()[1])
    sys.exit()