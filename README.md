# apartment-notifyer
 
## What is it
apartment-notifyer is a python tool that send a push notification via pushover if an apartment is available.

## How to use it
### Windows
1) Create python3 _venv_  and run `pip install -r requirements.txt` to install required modules.
2) Edit config in `apartment-notifyer.py`.
3) Create Task in Task Scheduler to run at a interval.
4) Set action to start `C:\path-to-venv\Scripts\python.exe` with argument `"C:\path\to\apartment-notifyer\apartment-notifyer.py"`

### macOS
1) Create python3 _venv_  and run `pip install -r requirements.txt` to install required modules.
2) Edit config in `apartment-notifyer.py`.
2) Create a LaunchAgent in `/Library/LaunchAgents/com.cr3ation.application-notifyer.plist` and execute the script

## Notifications
Is sent once per day if number of apartments is `>0`.

A new notification will be sent if if number of available goes from `1` to `2` to `...` for a given day.
