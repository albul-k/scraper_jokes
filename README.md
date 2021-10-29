# Jokes scraper

## Database description

### Table name: `joke`

* id: integer
* theme: varchar
* text: varchar
* rating: integer

### Example of fetching `jokes.db`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///jokes.db')
session = sessionmaker(bind=engine)

sql_query = 'SELECT * FROM joke'
rs = session().execute(sql_query)

for record in rs.fetchall():
    # your code
    pass
```
