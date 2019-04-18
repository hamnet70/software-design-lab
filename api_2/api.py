from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime


app = Flask(__name__)

app.config["DEBUG"] = True
app.config["STATIC_FOLDER"] = 'static'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def home():

    conn = sqlite3.connect("presidents3.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute("SELECT * FROM presidents;")
    presidents = cur.fetchall()

#    presidents = [
#        {
#            "first":"George",
#            "last":"Washington",
#            "number": 1,
#            "terms": 2,
#            "wife":"Martha"},
#        {
#            "first":"John",
#            "last":"Adams",
#            "number":2,
#            "terms":1,
#            "wife":"Abigail"},
#        {
#            "first":"Thomas",
#            "last":"Jefferson",
#            "number":3,
#            "terms":2,
#            "wife":"no one"},
#        {
#            "first":"James",
#            "last":"Madison",
#            "number":4,
#            "terms":2,
#            "wife":"Dolley"},
#        {
#            "first":"James",
#            "last":"Monroe",
#            "number":5,
#            "terms":2,
#            "wife":"Elizabeth"},
#        {
#            "first":"John Quincy",
#            "last":"Adams",
#            "number":6,
#            "terms":1,
#            "wife":"Louisa"},
#        {
#            "first":"Andrew",
#            "last":"Jackson",
#            "number":7,
#            "terms":2,
#            "wife":"Rachel"},
#        {
#            "first":"Martin",
#            "last":"Van Buren",
#            "number":8,
#            "terms":1,
#            "wife":"Hannah"},
#    ]

    return render_template('home.html', presidents=presidents)

@app.route('/blog', methods=["GET", "POST"])
def blog():
    if request.method == 'POST':
        post = request.form['post']
        posttime = datetime.datetime.now()
        username = request.form['username']

        conn = sqlite3.connect("presidents4.db")
        conn.row_factory = dict_factory
        cur = conn.cursor()
        cur.execute("INSERT INTO blogs (posttime, username, post) VALUES (?, ?, ?)",
                    (posttime, username, post))
        conn.commit()
        return redirect(url_for("home"))
  
    return render_template("blog.html")

@app.route('/blog_roll', methods=["GET"])
def roll():
    conn = sqlite3.connect("presidents4.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute("SELECT * FROM blogs;")
    blogs = cur.fetchall()

    return render_template('blog_roll.html', blogs=blogs)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        passwrd = request.form['passwrd']
        passwrd_renter = request.form['passwrd_reenter']

        conn = sqlite3.connect("presidents4.db")
        conn.row_factory = dict_factory
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, passwrd) VALUES (?, ?)",
                    (username, passwrd))
        conn.commit()
        return redirect(url_for("blog_roll"))
   
    return render_template("signup.html")


@app.route('/pic')
def pic():
    return render_template("pic.html")

app.run()
