from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CafeForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kdlKSPAD9809usd9SDPHJijoi'

Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    map_url = db.Column(db.String, unique=True, nullable=False)
    img_url = db.Column(db.String, unique=True)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes')
def cafes():
    data = Cafe.query.all()
    return render_template('cafe.html', list_of_cafes=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()

    if form.validate_on_submit():
        if form.has_sockets.data == 'True':
            sockets = 1
        else:
            sockets = 0

        if form.has_toilets.data == 'True':
            toilets = 1
        else:
            toilets = 0

        if form.has_wifi.data == 'True':
            wifi = 1
        else:
            wifi = 0

        if form.can_take_calls.data == 'True':
            calls = 1
        else:
            calls = 0

        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=sockets,
            has_toilet=toilets,
            has_wifi=wifi,
            can_take_calls=calls,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/delete/<int:cafe_id>')
def delete(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()

    return redirect(url_for('cafes'))


if __name__ == '__main__':
    app.run(debug=True)
