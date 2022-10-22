import requests
from datetime import datetime, timedelta
import json

Proxy = "https://index.golang.org/index"
timefmt = "%Y-%m-%dT%H:%M:%S.%fZ"
start_stamp = datetime(2017, 1, 1)
step = timedelta(days=7)
end_stamp = datetime.today()


def GetPackages(timestamp: datetime) -> set:
    d = timestamp.strftime(timefmt)
    body = requests.get(Proxy, {"since": d})
    strings = body.text.split()
    packages = set()
    for s in strings:
        p = json.loads(s)
        packages.add(p["Path"])
    return packages
