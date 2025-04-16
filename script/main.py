from flask import Flask, render_template
import dbOperations;

#potrei creare un sito web in cui viene usato il jwt token per accedere al sito e fare poi cose

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")    
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/candidature")
def candidature():
    return render_template("tabellaCandidature")

@app.route("/settings")
def settings():
    #qui dovrei inserire il file excel con le candidature e dovrebbero apparire nella pagina candidature
        return render_template("settings.html") 

if __name__ == "__main__":
    app.run(debug=True)