# We import Flask
from flask import Flask, render_template,jsonify
import json
from pymongo import MongoClient
from connections import readMongoCloud
import RE_data_cleaner
    
# We create a Flask app
app = Flask(__name__)

# We establish a Flask route so that we can serve HTTP traffic on that route 
@app.route('/')
def home():
    # We hardcode some information to be returned
    return render_template('index.html')

@app.route('/map.html')
def map():
    # We hardcode some information to be returned
    return render_template('map.html')

@app.route("/readData")
def read():
    db_df = readMongoCloud("Real_Estate","San_Fran")
    
    return jsonify(db_df.to_dict('records'))

@app.route("/DEEP")
def cleaner(): #JSON OF CLEANED
    
    DEEP_df = RE_data_cleaner.RE_cleaner()

    geeks_object = DEEP_df.to_html() 
  
    return geeks_object

    #return jsonify(DEEP_df.to_dict('records')) #UNCOMMENT WHEN READY

    #CONNECT TO CONNECTIONS.PY AND UPLOAD CLEANED DATA TO MONGO CLOUD

# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html

if __name__ == '__main__':
    app.run(debug=True)