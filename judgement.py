from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)
    # the actual "thing" containing the list of users queried from the DB is users

if __name__ == "__main__":
    app.run(debug = True)
