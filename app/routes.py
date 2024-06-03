from flask import render_template,url_for,flash,redirect,request
from app.form import RegistrationForm,LoginForm
from app import app,bcrypt,db
from app.models import User
from flask_login import login_user,logout_user,current_user,login_required


    
posts = [
    {"author":"Bett",
     "title":"Blog post 1",
     "content":"My first blog",
     "date_posted":"May 22, 2024"},
     {"author":"Benz",
     "title":"Blog post 2",
     "content":"My second blog",
     "date_posted":"May 25, 2024"},
     {"author":"Naomi",
     "title":"Blog post 3",
     "content":"My third blog",
     "date_posted":"May 29, 2024"},
]

@app.route("/")   
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title="About")


@app.route("/register",methods=["POST","GET"])   
def register():
    if current_user.is_authenticated:
      return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created successfully.Please login!","success")
        return redirect(url_for('login'))    #name for the function
    return render_template("register.html", title="Register", form=form)

@app.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
      return redirect(url_for("home"))
    form = RegistrationForm()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Get the first user
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next else redirect(url_for('home'))
        else:
          flash("Login unsuccessful.Please check username and password!","danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title='Account')

