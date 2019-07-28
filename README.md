# ical_filter

## description

Process upstream `.ics` files and serve it with flask.

## usage

```bash
cp config.py.sample config.py
vim config.py

docker build -t "ical_filter" .
./run.sh # you can change port mapping
```

Access the filtered ics by `http://127.0.0.1:5001/<key>/filtered.ics`.
