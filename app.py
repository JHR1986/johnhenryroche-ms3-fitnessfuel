import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# App route for home page
@app.route("/")
def home():
    return render_template("index.html", page="home")


# App route for phrases page
@app.route("/get_phrases")
def get_phrases():
    phrases = list(mongo.db.phrases.find())
    return render_template("phrases.html", phrases=phrases, page="get_phrases")


# App route for search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    phrases = list(mongo.db.phrases.find({"$text": {"$search": query}}))
    return render_template("phrases.html", phrases=phrases)


# App route for register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("This Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # Put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Your registration was successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", page="register")


# App route for login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # Ensure that the hashed password matches the users input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password match
                flash("An incorrect Username and/or Password was entered!")
                return redirect(url_for("login"))

        else:
            # The username does not exist
            flash("An incorrect Username and/or Password was entered!")
            return redirect(url_for("login"))

    return render_template("login.html", page="login")


# App route for profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, page="profile")

    return redirect(url_for("login"))


# App route for logout
@app.route("/logout")
def logout():
    # Remove the user from the session cookie
    flash("You have been successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# App route for add phrase page
@app.route("/add_phrase", methods=["GET", "POST"])
def add_phrase():
    if request.method == "POST":
        phrase = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.insert_one(phrase)
        flash("Phrase Successfully Added!")
        return redirect(url_for("get_phrases"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_phrase.html", categories=categories, page="add_phrase")


# App route for edit phrase page
@app.route("/edit_phrase/<phrase_id>", methods=["GET", "POST"])
def edit_phrase(phrase_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "english_name": request.form.get("english_name"),
            "korean_name": request.form.get("korean_name"),
            "brief_description": request.form.get("brief_description"),
            "created_by": session["user"],
        }
        mongo.db.phrases.update({"_id": ObjectId(phrase_id)}, submit)
        flash("Phrase Successfully Updated!")

    phrase = mongo.db.phrases.find_one({"_id": ObjectId(phrase_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_phrase.html", phrase=phrase, categories=categories)


# App route for delete phrase function
@app.route("/delete_phrase/<phrase_id>")
def delete_phrase(phrase_id):
    mongo.db.phrases.remove({"_id": ObjectId(phrase_id)})
    flash("Phrase Successfully Deleted!")
    return redirect(url_for("get_phrases"))


# Renders a 404 error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# Renders a 500 error
@app.errorhandler(500)
def something_wrong(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
