from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session
)

from models import db, User

app = Flask(__name__)

app.secret_key = "atm-secret"

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///atm.db"

db.init_app(app)


with app.app_context():

    db.create_all()

    if not User.query.first():

        db.session.add_all([

            User(
                username="user1",
                pin="1234",
                balance=1000
            ),

            User(
                username="user2",
                pin="2222",
                balance=2000
            ),

            User(
                username="user3",
                pin="3333",
                balance=3000
            )
        ])

        db.session.commit()


@app.route(
    "/",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        user = User.query.filter_by(
            username=request.form["username"]
        ).first()

        if user and user.pin == request.form["pin"]:

            session["user"] = user.id

            return redirect(
                "/dashboard"
            )

    return render_template(
        "login.html"
    )


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    user = User.query.get(
        session["user"]
    )

    return render_template(
        "dashboard.html",
        user=user
    )


@app.route("/deposit", methods=["POST"])
def deposit():

    user = User.query.get(session["user"])

    amount = request.form.get("amount")

    if not amount or amount.strip() == "":
        return redirect("/dashboard")

    amount = int(amount)

    if amount > 0:
        user.balance += amount
        db.session.commit()

    return redirect("/dashboard")


@app.route("/withdraw", methods=["POST"])
def withdraw():

    user = User.query.get(session["user"])

    amount = request.form.get("amount")

    if not amount or amount.strip() == "":
        return redirect("/dashboard")

    amount = int(amount)

    if amount > 0 and amount <= user.balance:
        user.balance -= amount
        db.session.commit()

    return redirect("/dashboard")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


app.run(host="0.0.0.0", port=5000, debug=True)
