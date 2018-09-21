import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from scrapping import scrape
from mongoConnections import FireUpMongo, addData
from flask_pymongo import PyMongo

from helpers.fb_helpers import login

app = Flask(__name__)

app.config.from_pyfile('config.cfg')  # Using the config file for setting up

ALLOWED_EXTENSIONS = set(['csv'])
# debug: reload jinja templates
app.jinja_env.auto_reload = True

# remove cache limit (default is 50 templates)
app.jinja_env.cache = {}

# Pymongo Connections
mongoConnections = PyMongo(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    # get current jobs number
    # get last ID used
    #
    if request.method == 'POST':
        #TODO: check for username or password pass
        option = request.form.getlist('Radio')
        print(request.form.getlist('Radio'))
        #TODO: check for single link or file read
    #
    # elif request.method == 'GET':
    #     return render_template('index.html')

    # else render page with data from data base

    return render_template('index.html')

    #TODO: get previous scrapping data and put them in table

@app.route('/results', methods=['GET', 'POST'])
def results():
    _base_url = []

    if request.method == "POST":
        if request.form.get('Radio') == 'login1':               # login enabled
            _username = request.form.get('username')            # get input username
            _password = request.form.get('password')            # get input password
            login(_username, _password)                         # try to login to facebook
        elif request.form.get('Radio') == 'login2':             # login disabled
            pass                                                # do nothing

        # TODO: Post link (import)
        if request.form.get('postlink') == 'postLink1':         # single post link enabled
            _base_url.append(request.form.get('singlePost'))    # adds to list for scrapping
            print(_base_url)
        elif request.form.get('postlink') == 'postLink2':       # multiple link enabled
            # TODO: read csv file line by line and do scrapping
            pass

    # get the data and pass to template
    return render_template('results.html')

@app.route('/addJob')
def addJob():
    _jobs_number = "Jobs1"
    _id = 1
    _postLink = "https://facebook.com"
    _likers_name = ["James Mcglynn", "SH SU TA", "Saidul Islam"]
    _likers_profile_link = ["https://www.facebook.com/james.mcglynn.69", "https://www.facebook.com/sstanni00", "https://www.facebook.com/profile.php?id=100004007562558"]
    _likers_like = [["Bigs bee", "Lion", "Cat"], ["Azir", "Udyr", "Jax"], ["Ahri", "Nautilus", "Brand"]]
    _commenters_name = ["Tanvir Ruhan", "Anis Sinha", "Mehedi Hossain"]
    _commenters_profile_link = ["https://facebook.com/James", "https://facebook.com/sh_tanni", "https://facebook.com/saidul"]
    _commenters_like = []

    _collections = mongoConnections.db.main
    _collections.insert_one({
        "id": _id,
        "dateStamp": datetime.datetime.utcnow(),
        "postLink": f"{_postLink}",
        "Likers":{
            "Name": _likers_name,
            "profileLink": _likers_profile_link,
            "like": _likers_like
        },
        "Commenters": {
            "Name":[],
            "profileLink":[],
            "like":[]
        }
    })
    return 'Jobs added'

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')


def getApi():
    print('calling from api')




# TODO: another result page for taking from database





if __name__ == '__main__':
    app.run()

