from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_user_login():
    # I need to get the user login information from the login.html file
    return render_template("login.html")

@app.route("/", methods=["POST"])
def process_user_login():
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    print ("User email and password = ", user_email, " == ", user_password)
    user = model.session.query(model.User).filter_by(
                        email = user_email).first()
    if user is None:
        new_user = model.User(email = user_email, password = user_password)
        model.session.add(new_user)
        model.session.commit()
        # add the user to the data base
        # this is where I would add the user_email and user_password to the Users table
        print "%s : %s" % (new_user.email, new_user.password)
        return redirect("/user_list")
    else:
        if user.password != user_password:
            print "password entered does not match the value on the table"
            return render_template("login.html")
        else:
            print ("this should display the user list of ratings")
            return redirect("/user_list")
        

@app.route("/user_list")
def user_list():
    user_list = model.session.query(model.User).limit(15).all()
    return render_template("user_list.html", users=user_list)
    # the actual "thing" containing the list of users queried from the DB is users

if __name__ == "__main__":
    app.run(debug = True)
