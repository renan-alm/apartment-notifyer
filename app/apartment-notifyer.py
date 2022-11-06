# -*- coding: utf-8 -*-
import os
import http.client, urllib
import json
import requests
from pathlib import Path
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
url = "https://minasidor.wahlinfastigheter.se/rentalobject/Listapartment/published?sortOrder=NEWEST"
resp = requests.get(url)
data = resp.json()

apartments = json.loads(data["data"])
apartments_found = len(apartments)

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
        print(f"{timestamp} | {apartments_found} lägenheter | Nothing to push")
        os._exit(0)
except:
    print("{} | An error was thrown".format(timestamp))

# Send push
if apartments_found > 0:
    # Pushover
    ## Message
    message = "Intresseanmäl på https://minasidor.wahlinfastigheter.se/ledigt/lagenhet"
    for apartment in apartments:
        message = message + f"""

---------------------------------------------------
💵    <b>{apartment["Cost"]} kr  *  {apartment["Size"]} m²</b>
🏠    {apartment["Adress1"]}
🗺️    {apartment["AreaName"]}
"""
    ## Send
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
        "token": _TOKEN,
        "user": _KEY,
        "title": f"{apartments_found} nya lägenheter",
        "message": message,
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

    print(f"{timestamp} | {apartments_found} lägenheter | Pushover message sent")
    log("{};{}".format(date, apartments_found))
