#!/usr/bin/env python3

import cgi
import cgitb
import re
import os

cgitb.enable()

print("Content-Type: text/html\n")

EMAIL_FILE = "/var/www/comingsoon/emails.txt"
IP_FILE = "/var/www/comingsoon/ips.txt"

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

form = cgi.FieldStorage()
email = form.getvalue("email")
ip_address = os.environ.get('REMOTE_ADDR', 'Unknown')

if email and is_valid_email(email):
    try:
        os.makedirs(os.path.dirname(EMAIL_FILE), exist_ok=True)
        os.makedirs(os.path.dirname(IP_FILE), exist_ok=True)

        if os.path.exists(EMAIL_FILE):
            with open(EMAIL_FILE, "r") as f:
                existing_emails = f.read().splitlines()
            if email in existing_emails:
                print("You are already subscribed!")
                exit()
        if os.path.exists(IP_FILE):
            with open(IP_FILE, "r") as w:
                existing_ips = w.read().splitlines()
            if ip_address in existing_ips:
                print("One email is enough! try maybe later")
                exit()

        with open(EMAIL_FILE, "a") as f:
            f.write(email + "\n")

        with open(IP_FILE, "a") as f:
            f.write(ip_address + "\n")

        print("Thank you for subscribing!")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Invalid email address. Please try again.")
