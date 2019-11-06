# -*- coding: utf-8 -*-

from lxml import html
import requests
import os
import subprocess
from bs4 import BeautifulSoup
from pathlib import Path
from pushover import init, Client
from datetime import datetime


### Variables to be set
token = "<pushover-token>"
key = "<pushover-key>"

token = "agcgh6v4si3xv7ipwcka43d5mao8vj"
key = "uGEiRVhV1VSm8yUQCsqb5RcKJoMp38"

# Path to push_sent.txt
push_sent = "{}/push_sent.txt".format(Path(os.path.realpath(__file__)).parent)

page = requests.get('https://wahlinfastigheter.se/lediga-objekt/lokaler/')

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(page.text, "lxml")

print(soup.prettify())
# print(u"{} funna: {}".format(type, total))

