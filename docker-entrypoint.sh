#!/bin/bash

echo ""
echo ""

APP="/app/apartment-notifyer.py"

# Validate parameters
if [ -z "$PUSHOVER_TOKEN" ]; then
    echo "Missing: Pushover token. Use '-e PUSHOVER_TOKEN=<token>'"
    exit 1
fi

if [ -z "$PUSHOVER_KEY" ]; then
  echo "Missing: Pushover key. Use '-e PUSHOVER_KEY=<key>'"
  exit 1
fi

echo "Pushover key: $PUSHOVER_KEY"
echo "Pushover token: $PUSHOVER_TOKEN"
echo "Update interval: $UPDATE_INTERVAL"
echo ""

# Edit stuff
sed -i "s/<pushover-token>/$PUSHOVER_TOKEN/" $APP
sed -i "s/<pushover-key>/$PUSHOVER_KEY/" $APP

while [ 1 ]
do
  python3 $APP
  sleep $UPDATE_INTERVAL
done


# Hand off to the CMD
exec "$@"
