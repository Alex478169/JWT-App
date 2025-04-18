from flask import Flask, render_template, request
from dbOperations import connect, showValues
from config import load_config
import psycopg2

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

@app.route("/candidature", methods=["GET", "POST"])
def candidature():
    try:
        with psycopg2.connect(**config) as conn:
            applicationDates=showValues(config, "application_date")
            contactsEmail = showValues(config, "contact_email")
            companyNames = showValues(config, "company_name")
            jobtitles = showValues(config, "job_title")
            urlJobs = showValues(config, "job_url")
            resumeNames = showValues(config, "resume_name")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    #Io penso che 
    return render_template("tabellaCandidature.html", applicationDates=applicationDates, contactsEmail=contactsEmail, companyNames=companyNames, jobtitles=jobtitles, urlJobs=urlJobs, resumeNames=resumeNames)
    

@app.route("/settings")
def settings(): 
    
    #qui dovrei inserire il file excel con le candidature e dovrebbero apparire nella pagina candidature
        return render_template("settings.html") 

if __name__ == "__main__":
    config = load_config()
    connect(config)
    app.run(debug=True)

