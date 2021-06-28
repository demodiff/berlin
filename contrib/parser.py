#!/usr/bin/env python3

from bs4 import BeautifulSoup
import json
import jsonlines
from datetime import datetime

if __name__ == "__main__":
    filename = "data/scraped.html"
    with open(filename, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        table = soup.findAll("table")
        results = []
        for line in table:
            entries = line.findAll("tr")
            for entry in entries[1:-1]: # remove first and last empty entry
                dates = entry.find("td", {"headers": "Datum"})
                if dates is not None:
                    dates = dates.get_text()

                starts = entry.find("td", {"headers": "Von"})
                if starts is not None:
                    starts = starts.get_text().replace("'", '"')

                ends = entry.find("td", {"headers": "Bis"})
                if ends is not None:
                    ends = ends.get_text().replace("'", '"')

                topics = entry.find("td", {"headers": "Thema"})
                if topics is not None:
                    topics = topics.get_text().replace("'", '"')

                zips = entry.find("td", {"headers": "PLZ"})
                if zips is not None:
                    zips = zips.get_text().replace("'", '"')

                places = entry.find("td", {"headers": "Versammlungsort"})
                if places is not None:
                    places = places.get_text().replace("'", '"')

                routes = entry.find("td", {"headers": "Aufzugsstrecke"})
                if routes is not None:
                    routes = routes.get_text().replace("'", '"')

                starts = str(datetime.strptime(dates + " " + starts, '%d.%m.%Y %H:%M').isoformat())
                ends = str(datetime.strptime(dates + " " + ends, '%d.%m.%Y %H:%M').isoformat())

                results.append(
                    {
                        "start": starts,
                        "end": ends,
                        "topic": topics,
                        "zip": zips,
                        "place": places,
                        "route": routes
                    }
                )

                with open("data/parsed.jsonl", "w") as writer:
                    for result in results:
                        json.dump(result, writer)
                        writer.write('\n')
