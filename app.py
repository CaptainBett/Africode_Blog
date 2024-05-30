from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f7927fd62f53d171e842d8dfc31d54b'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account for {form.username.data} has been created successfully!","success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")   
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True,port=5007)
















































