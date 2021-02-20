# -*- coding: utf-8 -*-
import os
import requests
from lxml import html
from pathlib import Path
from pushover import init, Client
from datetime import datetime

# Config
_TOKEN = "<pushover-token>"
_KEY = "<pushover-key>"

# End of config

date = datetime.now().strftime("%Y-%m-%d")  # Eg. 2019-10-23
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M') # Eg. 2021-02-20 13:37
log_file = "{}/notifications.log".format(Path(os.path.realpath(__file__)).parent)

def log(message):
    f = open(log_file, "a+")
    f.write("{}\n".format(message))
    f.close()

# Scrape HTML
page = requests.get('https://wahlinfastigheter.se/lediga-objekt/lagenheter/')
tree = html.fromstring(page.content)

apartments_found = int(tree.xpath('//span[@class="total-article"]/text()')[1])  # Int
type = tree.xpath('//span[@class="term-name"]/text()')[1]                       # Förråd, Lägenheter, Lokaler, P-platser

print(u"{} | {} {}".format(timestamp, apartments_found, type))

# Logic - send push or not
try:
    last_run = None
    last_run_apartments_found = None

    # Create logfile non existing
    if os.path.exists(log_file) == False:
        log("date;apartments_found")
        log("{};{}".format(date, apartments_found))

    # Read last line in log
    with open(log_file, 'r') as f:
        lines = f.read().splitlines()
        last_run = lines[-1][:10]
        last_run_apartments_found = int(lines[-1][11:])

    # New day? New log entry.
    if date != last_run:
        log("{};{}".format(date, apartments_found))

    # Exit if nothing to push
    if date == last_run and apartments_found <= last_run_apartments_found:
        print("%s | Nothing to push." % timestamp)
        os._exit(0)
except:
    print("%s | An error was thrown" % timestamp)

# Send push
if apartments_found > 0:
    # Pushover
    init(_TOKEN)
    Client(_KEY).send_message(u"Intresseanmäl på https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
                              .format(apartments_found), title="{} nya lägenheter".format(apartments_found))

    print("%s | Pushover message sent" % timestamp)
    log("{};{}".format(date, apartments_found))
