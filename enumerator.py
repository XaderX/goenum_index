from datetime import datetime, timedelta
import json

import requests

Proxy = "https://index.golang.org/index"
timefmt = "%Y-%m-%dT%H:%M:%S.%fZ"


def GetPackagesByPeriod(since: datetime, end: datetime, step: timedelta) -> set:
    packets = set()
    while since < end:
        packets.update(GetPackages(since))
        since += step
    return packets


def GetPackages(timestamp: datetime) -> set:
    d = timestamp.strftime(timefmt)
    body = requests.get(Proxy, {"since": d})
    strings = body.text.split()
    packages = set()
    for s in strings:
        p = json.loads(s)
        packages.add(p["Path"])
    return packages
