#import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create a flask instance
app = Flask(__name__)

#establish Mongo connection using PyMongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    #find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
    

    #return template and data
    return render_template("index.html", mars = mars)
    

#route that will trigger the scrape function

@app.route("/scrape")
def scrape():
    
    mars = mongo.db.mars

    #run the scrape function and save the results to a variable

    mars_data = scrape_mars.scrape()

    #update the Mongo database using update and upsert = True
    mars.update({}, mars_data, upsert = True)

    # Redirect back to home page
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)
