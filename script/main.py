from dbOperations import *
from config import load_config
#from flask_jwt_extended import JWTManager, create_access_token
#from authlib.integrations.flask_client import OAuth
import os
from flask import Flask, render_template, request, url_for
import psycopg2
import pandas as pd

app = Flask(__name__)

#imposta la chiave segreta per le sessioni Flask utilizzando una variabile d'ambiente
'''app.secret_key = os.environ.get("FLASK_SECRET_KEY", "NadaAmePiruAttoCarrell1253484")
#configurazione delle chiavi di sicurezza utilizzando variabili d'ambiente
app.config["secret"] = os.environ.get("secret", "v7+MPnCh66xstznZq9mJ7nMMCrXxmdZrVIxrHuUdr18K1v0gi2yV2sSudD2ohb8yfGM8AuxbyKjiz9BwcSOoRg==")

#inizializza JWT
jwt = JWTManager(app)

#autenticazione con linkedin
linkedin = oauth.register(
    "linkedin",
    client_id = app.config["LINKEDIN_CLIENT_ID"]
    client_secret=app.config["LINKEDIN_CLIENT_SECRET"]
    authorize_url="https://www.linkedin.com/oauth/v2/authorization"
    authorize_params=None,
    access_token_url="https://www.linkedin.com/oauth/v2/accessToken",
    access_token_params=None,
    refresh_token_url=None,
    api_base_url='https://api.linkedin.com/v2/',
    client_kwargs={'scope': 'r_liteprofile r_emailaddress w_member_social'}
)'''

#pagina di registrazione
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


#pagina di login
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

#pagina di home
@app.route("/home")
def home():
    return render_template("home.html")

#opzioni per la tabella candidature
@app.route("/options", methods=['GET', 'POST'])
def candidatureOptions():
    #io qui, a partire dal df.columns[0]momento in cui ho inserito un file, ed il formato è corretto, io dovrei passare il file (utilizzare la funzione fromExcelToSQL()) e caricarlo nel database
    #la conversione del csv è già fatto, ma ora devo prendere il file csv e caricarlo. dovrei prendere solamente il percorso file e bon, risolta la situazione
    if request.method == "POST":
        File="/home/ale/.cache/.fr-L3ZH42/Jobs/uarewelcome.xlsx"
        fromExcelToSQL(config, File)
        archivio = request.files.get("archive")
        '''if archivio.filename != "":
            print(archivio.filename)'''
        return render_template("options.html")
    return render_template("options.html")

#pagina tabella candidature
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
    
    try:
        if viewDataTable(config, "job_application") is not None:
            pass
        else:
            fromCSVToSQL(file, table)
            return render_template("tabellaCandidature.html", applicationDates=applicationDates, contactsEmail=contactsEmail, companyNames=companyNames, jobtitles=jobtitles, urlJobs=urlJobs, resumeNames=resumeNames)
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)
        
    return render_template("tabellaCandidature.html", applicationDates=applicationDates, contactsEmail=contactsEmail, companyNames=companyNames, jobtitles=jobtitles, urlJobs=urlJobs, resumeNames=resumeNames) 

if __name__ == "__main__":
    config = load_config()
    connect(config)
    app.run(debug=True)




"""
def login_linkedin():
    redirect_uri = url_for('authorize_google', _external=True)
    nonce = secrets.token_urlsafe(16)  # Genera un nonce casuale
    session['oauth_nonce'] = nonce  # Salva il nonce nella sessione
    return google.authorize_redirect(redirect_uri, nonce=nonce)

# Callback per Google OAuth
@app.route('/authorize/google')
def authorize_google():
    try:
        token = google.authorize_access_token()
        nonce = session.pop('oauth_nonce', None)
        if not nonce:
            return jsonify({'msg': 'Nonce non trovato in sessione, riprovare'}), 400
        
        user_info = google.parse_id_token(token, nonce=nonce)
        
        # Verifica se l'utente esiste già nel database
        user = users.find_one({'email': user_info['email']})
        
        if not user:
            # Se l'utente non esiste, registralo
            users.insert_one({'email': user_info['email'], 'password': None})

        # Genera un token JWT
        access_token = create_access_token(identity={'email': user_info['email']})
        return jsonify({'token': access_token}), 200

    except Exception as e:
        print(f"Errore durante l'autenticazione con Google: {e}")
        return jsonify({'msg': 'Errore durante l\'autenticazione con Google', 'error': str(e)}), 500

"""