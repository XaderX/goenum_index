import enumerator

from datetime import datetime, timedelta
import argparse
import logging

if __name__ == "__main__":
    today = datetime.today().isoformat()
    parser = argparse.ArgumentParser(description="Enumerate go-packages on https://index.golang.org/index for download with Athens")
    parser.add_argument("output", type=str, default="go_packages.txt", help="Filename for saving list of names packages")
    parser.add_argument("--since", type=str, default="2017-01-01T00:00:00", help="Date for begin fetch packages, using 'since' query on site")
    parser.add_argument("--step", type=int, default=30, help="Size of step for enumeration in days")
    parser.add_argument("--end", type=str, default=today, help="End date for enumeration")
    parser.add_argument("-v", "--verbose", action='store_true', help="Verbose")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    step = timedelta(days=args.step)
    since = datetime.fromisoformat(args.since)
    end = datetime.fromisoformat(args.end)
    packets = enumerator.GetPackagesByPeriod(since, end, step)
    with open(args.output, "w") as f:
        f.write("\n".join(packets))
        f.close()
