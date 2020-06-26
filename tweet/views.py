from.database import db
from.app import app
from flask import Flask, render_template, redirect, request,session
from.models import User,Tweet

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == 'POST' :
       fname = request.form['fname'] 
       email = request.form['email']
       uname = request.form['uname']
       pwd = request.form['pass']

       user = User(full_name=fname,email=email,username=uname,password=pwd)

       db.session.add(user)
       db.session.commit()

       return redirect('/')
    else:
        return render_template('register.html')

@app.route("/login", methods=['POST','GET'])
def login():

    if request.method == 'POST':
        login = User.query.filter_by(username=request.form['username'],password=request.form['password']).first()

        if login:
            session['id'] = login.id
            return redirect('/tweet')
        else:
            return 'Error'
    else:
        return render_template('login.html')

@app.route("/tweet",methods=['POST','GET'])
def tweet():
    id = session['id']
    tweet = Tweet.query.order_by(Tweet.id.desc()).all()
    login = User.query.filter_by(id=id).first()

    if request.method == 'POST':
        
        say = request.form["say"]
        tweet = Tweet(user_id=id,msg=say)

        db.session.add(tweet)
        db.session.commit()

        return redirect('/tweet')
    else:
        return render_template('timline.html', tweets=tweet, login=login)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
@app.route('/deletetweet/<int:id>')
def deleteTweet(id):
    tweet_to_delete = Tweet.query.get_or_404(id)

    try:
        db.session.delete(tweet_to_delete)
        db.session.commit()

        return redirect('/tweet')
    except:
        return'Erorr'
@app.route('/updatetweet/<int:id>',methods=['POST','GET'])
def updatetweet(id):
    tweet = Tweet.query.get_or_404(id)

    if request.method =='POST':
        tweet.msg = request.form["say"]

        try:
            db.session.commit()
            return redirect('/tweet')
        except:
            return "error"
    else:
       return render_template('updatetweet.html',tweet=tweet)

@app.route('/updateprofile/<int:id>',methods=['POST','GET'])
def updateprofile(id):
    user = User.query.get_or_404(id)

    if request.method =='POST':
        user.full_name = request.form['fname'] 
        user.email = request.form['email']
        user.password = request.form['pass']

        try:
            db.session.commit()
            return redirect('/tweet')
        except:
            return "error"
    else:
       return render_template('updateprofile.html',user=user)

@app.route('/deleteaccount/<int:id>')
def deleteaccount(id):
    # tweet_to_delete = Tweet.query.filter_by(user_id=id).all()
    user_to_delete = User.query.get_or_404(id)

    try:
        # db.session.delete(tweet_to_delete)
        # db.session.commit()

        db.session.delete(user_to_delete)
        db.session.commit()

        return redirect('/logout')
    except:
        return'Erorr'
@app.route('/viewall')
def viewall():
    # query().all() <--- displays everything; display ALL records; select * from user
    user = User.query.order_by(User.id).all()

    return render_template('viewall.html',users=user)
@app.route('/viewuser/<int:id>')
def viewuser(id):
    user = User.query.filter_by(id=id).first()
    tweet = Tweet.query.filter_by(user_id=id).order_by(Tweet.id.desc()).all()
    return render_template('viewuser.html',user=user,tweet=tweet)







