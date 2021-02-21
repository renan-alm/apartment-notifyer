# apartment-notifyer
A python tool that sends a push notification via pushover if a new apartment becomes available on Wåhlin Fastigheter.

## Installation
### Windows
1) Create python3 _venv_  and run `pip install -r requirements.txt` to install required modules.
2) Edit config in `apartment-notifyer.py`.
3) Create Task in Task Scheduler to run at a interval.
4) Set action to start `C:\path-to-venv\Scripts\python.exe` with argument `"C:\path\to\project\apartment-notifyer.py"`

### macOS
1) Create python3 _venv_  and run `pip install -r requirements.txt` to install required modules.
2) Edit config in `apartment-notifyer.py`.
2) Create a LaunchAgent in `/Library/LaunchAgents/com.cr3ation.application-notifyer.plist` and execute `/path/to/project/apartment-notifyer.py`

## Notifications
Is sent once per day if number of apartments is `>0`.
Another notification will be sent if number of available apartments goes from `1` to `2` to `...` on a given day.

## Docker
Install using `docker-compose` or by building the image from scratch. Examples below.

### Prerequisities
In order to run within a container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [macOS](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Install using docker-compose
Edit `docker-compose.yaml`. Add `PUSHOVER_TOKEN` and `PUSHOVER_KEY` and save. Then run
```shell
docker-compose up 
```

### Install using docker
#### Build image
```shell
docker build -t apartment-notifyer:latest . 
```

#### Run container
```shell
docker run -d -e PUSHOVER_TOKEN=<token> -e PUSHOVER_KEY=<key>  apartment-notifyer:latest
```

### Environment Variables
* `PUSHOVER_TOKEN` - Mandatory
* `PUSHOVER_KEY` - Mandatory
* `UPDATE_INTERVAL` - Optional. Default = 60 seconds.

### Volumes
* `/app/` - Entire project including logs

### Useful File Locations (inside container)
* `/app/apartment-notifyer.py` - Main application
* `/app/notifications.log` - Logs

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## Authors
* **Henrik Engström** - *Initial work* - [cr3ation](https://github.com/cr3ation)
See also the list of [contributors](https://github.com/cr3ation/apartment-notifyer/contributors) who 
participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
