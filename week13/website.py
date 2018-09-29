from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import datetime as dt
from imp import reload
import scrape_mars 
reload(scrape_mars)
import time
# %%
# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    marsinfo = mongo.db.marsinfo.find_one()
    return render_template('index.html', marsinfo = marsinfo)

@app.route('/scrape')
def scraper():
    marsinfo_data = scrape_mars.scrape_all()
    print('scraper start')
    marsinfo = mongo.db.marsinfo
   
    #time.sleep(30)
    print(marsinfo_data)
    marsinfo.update({}, marsinfo_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
