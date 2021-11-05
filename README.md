# Jokes scraper

## Description

Scraper collects jokes and saves them in sqlite database `jokes.db`

## Structure of `jokes.db`

* Table name: `joke`
  * `id` - integer
  * `theme` - varchar
  * `text` - varchar
  * `rating` - integer

## Example of fetching `jokes.db`

```python
import sqlite3 as sql


db_connect = sql.connect('jokes.db')
cur = db_connect.execute('SELECT * FROM joke')
rows = cur.fetchall()
cur.close()

for row in rows:
    # your code
    pass
```

## How to run scraper

```bash
git clone https://github.com/albul-k/scraper_jokes
cd scraper_jokes

python -m venv venv
source venv/bin/activate
## for Win
# source venv/Scripts/activate

pip install -r requirments.txt
python main.py
```

## Sources

* [anekdotme.ru](http://anekdotme.ru/)
