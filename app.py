from flask import Flask, render_template
import data
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html",
                           tours=data.tours,
                           subtitle=data.subtitle,
                           title=data.title,
                           description=data.description,
                           departures = data.departures,
                           )

@app.route('/departures/<departure>/')
def departures(departure):
    tours = data.tours
    dep = {}
    dep_price = []
    dep_night = []

    for tour in tours:
       if tours[tour]["departure"] == departure:
           dep[tour] = tours[tour]
           dep_price.append(tours[tour]["price"])
           dep_night.append(tours[tour]["nights"])

    return render_template("departure.html",
                           tours=dep,
                           title=data.title,
                           departures = data.departures,
                           departure = departure,
                           dep_price = dep_price,
                           dep_night = dep_night
                           )

@app.route('/tours/<id>/')
def tours(id):
    return render_template("tour.html",
                           tours=data.tours,
                           title=data.title,
                           departures = data.departures,
                           id = int(id))

app.run(debug=True)