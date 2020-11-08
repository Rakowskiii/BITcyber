from flask import render_template, render_template_string, request, redirect, url_for, make_response
from app import app, db
from app.models import Post, User, UserData
import os
import re
import urllib.parse

@app.after_request
def add_header(response):
    return response

@app.route("/")
def hello():
    return render_template("index.html",mockup=Post.query.all())

@app.route("/reset")
def reset():
    os.system("rm app/blog.sql && python3 add.py")
    rsp = make_response(redirect("/"))
    rsp.set_cookie("role","0")
    return rsp


@app.route("/cmsadmin", methods=["GET","POST"])
def admin():
    print(User.query.get(0).adm_blocked)
    if request.method == "POST":
        if request.form['activate'] == "tajnykoddoaktywacjiadmina":
            User.query.get(0).adm_blocked = False
            db.session.commit()
        return redirect(request.url)
    if request.cookies.get('role') == '5':
        return render_template('adm_page.html', logged_in=True,  active = (not User.query.get(0).adm_blocked))
    resp = make_response(render_template('adm_page.html', logged_in=False,  active = (not User.query.get(0).adm_blocked)))
    resp.set_cookie('role','0')
    return resp

@app.route("/post", methods=["GET","POST"])
def post():
    if request.method == "GET":
        if request.args.get('id') == "4c4be2dc-c3e9-401d-9127-b33befcd49ba" and request.args.get('file'):
            u = User.query.get(0)
            if not u.done:
                path = './uploaded/'+request.args.get('file')
                if os.path.isfile(path):
                    file = open(path,'r').read()
                else :
                    file = "File doesn't exist."
                if os.path.realpath(path) == '/etc/passwd':
                    u.done = True
                    db.session.commit()
                return render_template("path_trav/post_path_trav.html", post = Post.query.get(request.args.get("id")), ofile = file)
            elif not u.done2:
                print("lab 2")
                path = './uploaded/'+request.args.get('file')
                path = re.sub(r"\.\.\/","",path)
                print(path)
                if os.path.isfile(path):
                    file = open(path,'r').read()
                else :
                    file = "File doesn't exist."
                if os.path.realpath(path) == '/etc/passwd':
                    u.done2 = True
                    db.session.commit()
                return render_template("path_trav/post_path_trav.html", post = Post.query.get(request.args.get("id")), ofile = file)
            else :
                path = './uploaded/'+request.args.get('file')
                while re.findall(".\.\.\/",path) != list():
                    path = re.sub(r"\.\.\/","",path)
                path = urllib.parse.unquote_plus(path)
                path = urllib.parse.unquote_plus(path)
                print(path)
                if os.path.isfile(path):
                    file = open(path,'r').read()
                else :
                    file = "File doesn't exist."
                if os.path.realpath(path) == '/etc/passwd':
                    u.done = True
                    db.session.commit()
                return render_template("path_trav/post_path_trav.html", post = Post.query.get(request.args.get("id")), ofile = file)
        if request.args.get('id') == "ba1d889c-a14a-427d-b9a6-a4b7f43cf831":
            if  User.query.get(0).adm_blocked:
                return render_template('adm_blocked.html')
            else:
                if not request.args.get('zYb'):
                    return redirect(request.url+"&zYb=eydpZCc6MH0K")
                return render_template("idor.html", data = UserData.query.get(request.args['zYb']),post = Post.query.get(request.args.get("id")))
        return render_template("path_trav/post_path_trav.html", post = Post.query.get(request.args.get("id")))

    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url.split('&')[0]+"&uploaded=false")
        if file:
            filename = re.sub("\.\.\/","", file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url.split('&')[0]+"&uploaded=true")
    return not_found()

@app.errorhandler(404)
def not_found(e):
    return "<h1 align='center' style='padding-top:20' > Sadly, page was not found.</h1>\n"
