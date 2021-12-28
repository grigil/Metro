#!flask/bin/python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/metro"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    description = db.Column(db.String())
    image = db.Column(db.String())
    url = db.Column(db.String())

    def __init__(self, date, description, image, url):
        self.date = date
        self.description = description
        self.image = image
        self.url = url

    def __repr__(self):
        return f"<news {self.id}>"

@app.route('/metro/news', methods=['GET'])
def get_tasks():
    day = request.args.get('day', default=None, type=int)
    if day is None:
        return "please enter day parameter like /metro/news?day=5"
    else:
        date_end = datetime.today().strftime('%Y-%m-%d')
        date_start = (datetime.strptime(date_end, '%Y-%m-%d') - timedelta(day)).strftime('%Y-%m-%d')
        task = NewsModel.query.filter(NewsModel.date.between(date_start, date_end)).all()
        response = [{
            "date": news.date.strftime('%Y-%m-%d'),
            "description": news.description,
            "image": news.image,
            "url": news.url
        } for news in task]
        return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)