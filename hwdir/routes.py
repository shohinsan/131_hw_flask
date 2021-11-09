from flask import render_template, redirect

from hwdir import app, db
from hwdir.forms import TopCities
from hwdir.models import City


@app.route("/", methods=["POST", "GET"])
def home():
    title = "Top Cities"
    name = "Shohin"
    goo = "https://google.com"
    form = TopCities()
    if form.validate_on_submit():
        city = City(city_name=form.city_name.data,
                    city_rank=form.city_rank.data,
                    is_visited=form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        return redirect("/")
    cities = City.query.order_by(City.city_rank.asc()).all()
    return render_template("home.html",
                           title=title,
                           name=name,
                           form=form,
                           top_cities=cities,
                           google=goo)

