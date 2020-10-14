from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

#test
class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String(64), index=True, unique=True)
    link = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(128))
    logo = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.division)    



@app.after_request
def add_header(response):
    response.headers['X-Flag-Header'] = 'flag{m4st3r_1nt3rc3pt0r}'
    return response


@app.route("/")
def hello():
    return render_template("index.html",mockup=Division.query.all())

@app.route("/enroll", methods=['GET','POST'])
def enroll():
    if request.method == "GET":
        return render_template("enroll.html")
    if request.method == "POST":
        #POST
        return render_template("enrolled.html")

@app.route("/division") 
def user():
    if request.args.get("id") == "35":
        return "flag{n1c3_id0r}"
    try:
        _id=int(request.args.get("id"))
    except:
        return not_found(0)
    if _id >= len(Division.query.all()):
        return not_found(0)
    return render_template("user_page.html", div=Division.query.all()[_id])

@app.route("/about")
def about():
    return render_template("about_us.html", value = request.args.get("v"))

@app.route("/robots.txt")
def robots():
    return open("robots.txt","r").read()

@app.errorhandler(404)
def not_found(e):
    return "<h1 align='center'> Sadly, page was not found.</h1>\n<!-- TODO Prepare better error page-->\n<!-- flag{wh0_3v3n_r34d2_th0s3_c0mm3n7s}-->"



if __name__ == "__main__":
    app.run(port=8080, host="46.101.100.104")

#46.101.100.104
#TODO fix ip, port ^,8080