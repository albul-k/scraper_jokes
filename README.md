# Jokes scraper

## Database description

### Table name: `joke`

* id: integer
* theme: varchar
* text: varchar
* rating: integer

### Example of fetching `jokes.db`

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

## Sources

* [anekdotme.ru](http://anekdotme.ru/)
