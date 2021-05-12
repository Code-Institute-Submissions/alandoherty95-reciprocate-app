import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# pagination limit
PER_PAGE = 6


# flask app setup
app = Flask(__name__)
# config vars
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# pagination
# inspiration from https://betterprogramming.pub/simple-flask-pagination-example-4190b12c2e2e
def paginate(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


# routing

@app.route("/")
# recipes page
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    paginated_recipes = paginate(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html",
        recipes=paginated_recipes,
        pagination=pagination,
        page_heading="Browse All Recipes")


# search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({
        "$text": {"$search": query}}).sort("_id", -1))
    paginated_recipes = paginate(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html",
        recipes=recipes,
        paginated_recipes=paginated_recipes,
        pagination=pagination,
        page_heading="Displaying results for '{}'".format(query))


# registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in mongo db already
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Unfortunately, this username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into a session
        session["user"] = request.form.get("username").lower()
        flash("Registration complete!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username already exists in mongo db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensures hashed password is a match
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Good to see you again, {}!".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # hashed password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username does not exist in mongo db
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# user profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # takes username of session user from mongo db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # displays all recipes shared by session user
        user = mongo.db.users.find_one({"username": session["user"]})
        user = list(user)
        recipes = mongo.db.recipes.find(
            {"created_by": session["user"]})
        recipes = list(recipes)
        return render_template(
            "profile.html",
            username=username,
            recipes=recipes)
    else:
        return redirect(url_for("login"))


# log out
@app.route("/logout")
def logout():
    # removes user from current session
    flash("Log out successful. See you again soon!")
    session.pop("user")
    return redirect(url_for("get_recipes"))


# add new recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "created_by": session["user"],
            "image_url": request.form.get("image_url")
            }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you for contributing!")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_recipe.html", categories=categories)


# edit a recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "created_by": session["user"],
            "image_url": request.form.get("image_url")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe was successfully updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html",
        recipe=recipe, categories=categories)


# delete a recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe was successfully deleted")
    return redirect(url_for("get_recipes"))


# view categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add new recipe type
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash('Category successfully updated')
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash('Category was successfully deleted')
    return redirect(url_for("get_categories"))


# about
@app.route("/about")
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    # custom 404 error handling page
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    # custom 500 error handling page
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
