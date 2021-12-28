# Readme Metro project v0.1


## Usage

First setup your postgresql in parser.py and in app.py in config
```python
# BD connect app.py
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/metro"
# BD connect parser.py
connection = psycopg2.connect(database="metro", user="postgres", password="*****", host="localhost", port="5432")
```

Then you need to migrate BD

```python
flask db init
flask db migrate
flask db upgrade
```

Run parser.py to parse https://mosmetro.ru/news/

After this you need run docker-compose up, then push get request to server
for example "/metro/news?day=5"

![img.png](img.png)

This is what you should get by response

