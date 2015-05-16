from flask import Flask, request, render_template, g
from peewee import MySQLDatabase, Model, IntegerField, InternalError

import socket
import os


app = Flask(__name__)

mysqldb = MySQLDatabase(
    os.environ.get('DB_NAME'), 
    host=os.environ.get('DB_HOST'), 
    user=os.environ.get('DB_USER'), 
    password=os.environ.get('DB_PASS')
)


class Stats(Model):
    visits = IntegerField()
    class Meta:
        database = mysqldb        

try:
    Stats.create_table()
    Stats.insert(visits = 0).execute()
except (InternalError):
    print "Stats table exists, moving on"


@app.route('/', methods=['GET'])
def home():
    update = Stats.update(visits = Stats.visits + 1)
    update.execute()
    stat = Stats.get()
    hostname = socket.gethostname()
    return render_template('index.html', server=hostname, visits=stat.visits)


@app.before_request
def before_request():
    g.db = mysqldb
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')