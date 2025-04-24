from flask import Flask, render_template, request, url_for
from dbOperations import connect, showValues, insertValues, compareValues, fromCSVToSQL, viewDataTable, searchSomething
from config import load_config
import psycopg2
import pandas as pd

#potrei creare un sito web in cui viene usato il jwt token per accedere al sito e fare poi cose

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with psycopg2.connect(**config) as conn:
            if insertValues(config, username, password):
                return render_template("login.html")
            else:
                return render_template("register.html", error="registrazione non avvenuta") 
    
    return render_template("register.html")

@app.route("/login", methods=['POST', 'GET'])    
def login():
    with psycopg2.connect(**config) as conn:
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            
            if compareValues(config, username, password):
                return render_template("home.html")
            else:
                return render_template("login.html", error="credenziali errate")
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/options")
def candidatureOptions():
    return render_template("options.html")

@app.route("/candidature", methods=["GET"])
def candidature():
    file = "/home/ale/Downloads/Jobs/Job_Applications.csv"
    table = "job_application"

    company=request.form.get("company")
    email=request.form.get("email")
    
    if request.method == "GET":
        searchSomething(config, company)

    applicationDates= showValues(config, "application_date")
    contactsEmail = showValues(config, "contact_email")
    companyNames = showValues(config, "company_name")
    jobtitles = showValues(config, "job_title")
    urlJobs = showValues(config, "job_url")
    resumeNames = showValues(config, "resume_name")
    
    print(applicationDates)
    try:
        if viewDataTable(config, "job_application") is not None:
            pass
        else:
            fromCSVToSQL()
            return render_template("tabellaCandidature.html", applicationDates=applicationDates, contactsEmail=contactsEmail, companyNames=companyNames, jobtitles=jobtitles, urlJobs=urlJobs, resumeNames=resumeNames)
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)
        
    return render_template("tabellaCandidature.html", applicationDates=applicationDates, contactsEmail=contactsEmail, companyNames=companyNames, jobtitles=jobtitles, urlJobs=urlJobs, resumeNames=resumeNames) 

if __name__ == "__main__":
    config = load_config()
    connect(config)
    app.run(debug=True)

