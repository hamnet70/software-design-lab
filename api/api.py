#import flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return "<h1>The Presidential Database</h1><p>Welcome to my unfancy resource.</p>"

@app.route('/api/v1/resources/presidents/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('presidents.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_presidents = cur.execute('SELECT * FROM presidents;').fetchall()

    return jsonify(all_presidents)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/presidents', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    first_name = query_parameters.get('first_name')
    last_name = query_parameters.get('last_name')
    total_terms = query_parameters.get('total_terms')
    
    query = "SELECT * FROM presidents WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if first_name:
        query += ' first_name=? AND'
        to_filter.append(first_name)
    if last_name:
        query += ' last_name=? AND'
        to_filter.append(last_name)
    if not (id or first_name or last_name):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect ('presidents.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

    app.run()