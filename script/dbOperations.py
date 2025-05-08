import psycopg2
import pandas as pd
import numpy as np
from fileManipulator import *

def viewDataTable(config, table: str):
    """
    (view the table content)visualizza il contenuto di una tabella

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        table (str): nome della tabella

    returns:
        str: errore di connessione al database
    """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table};")
            values = cur.fetchall()
            return values
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def insertJobApplication(config, appDate: str, contEmail: str, compName: str, jobTitle: str, jobUrl: str, resName: str):
    """
    inserimento di una riga nella tabella job_applications

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        appDate: colonna di application_date
        contEmail: colonna di contact_email
        compName: colonna di company_name
        jobTitle: colonna di job_title
        jobUrl: colonna di job_url
        resName: colonna di resume_name

    returns:
        str: errore di connessione al database postgresql
    """
    try:
        with psycopg2.connect(**config) as conn:
            cur = psycopg2.cursor()
            cur.execute("INSERT INTO job_application(Application_Date, Contact_Email, Company_Name, Job_Title, Job_Url, Resume_Name) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');", appDate, contEmail, compName, jobTitle, jobUrl, resName)
            cur.commit()
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            return "Good job boy! you are connected to the database!"
    except (psycopg2.DatabaseError, Exception) as error:
            return str(error)

def showValues(config, column: str):
    """
    mostra i valori di una colonna specifica

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        column: nome di una colonna
    
    returns:
        str: errore di connessione al database
    """
    try:
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute(f"select {column} from job_application;")
            rows = cur.fetchall()
            return rows
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def insertValues(config, username:str, password:str):
    """
    esegue la registrazione di un utente

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        username: nome utente dell'utente registrato
        password: password dell'utente registrato

    returns:
        str: errore di connessione al database postgresql
    """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            values = viewDataTable(config, "users")
            for row in values:
                if username in row and password in row :
                    return "l'utente esiste già, attaccati"
                else:
                    cur.execute("INSERT INTO users(id, username, password) VALUES ('{0}', '{1}');", username, password)
                    conn.commit()
                    return "hai inserito un nuovo utente"
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def compareValues(config, username:str, password:str):
    """
    compara la password di un utente specifico con quello inserito
    
    args:
        config: file di configurazione che permette la connessione con il database postgresql
        username: username di un utente usato per cercare una password specifica
        password: password inserita dall'utente nella schermata di login che viene comparata con la password dell'utente specifico
    
    returns:
        str: l'errore relativo alla connessione al database postgresql
    """
    try:
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute("SELECT password FROM users WHERE username='{0}'", username)
            value = cur.fetchone()

            if password in value[0]:
                return True
            else:
                return False

    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def fromCSVToSQL(config, file: str):
    """
    imagazzina i dati presenti in un file CSV (.csv) all'interno di un database postgresql 

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        file(str): nome del file da cui prendere i dati da inserire nel database 

    returns:
        str: errore di connessione al database postgresql
    """
    insert_queries=[]
    
    df = pd.read_csv(file)

    df.loc[df["Application Date"] == "9/9/24, 8:21 AM", "Company Name"] = "Tecne - Gruppo Autostrade per Italia"
    df.to_csv(file)
    for _,row in df.iterrows():
        application_date = row["Application Date"].replace("'", "''")
        contact_email = row["Contact Email"].replace("'", "''")
        company_name = row["Company Name"].replace("'", "''")
        job_title = row["Job Title"].replace("'", "''")
        job_url = row["Job Url"].replace("'", "''")
        resume_name = row["Resume Name"].replace("'", "''")
        try:
            with psycopg2.connect(**config) as conn:
                cur = conn.cursor()
                for sql in insertQueries:    
                    insertJobApplication(config, application_date, contact_email, company_name, job_title, job_url, resume_name)
        except (psycopg2.DatabaseError, Exception) as error:
            return str(error)
    
    return "tutto è andato buon fine"

def fromExcelToSQL(config, file:str):
    """
    imagazzina i dati presenti in un file Excel (.xslx) all'interno di un database postgresql 

    args:
        config: file di configurazione che permette la connessione con il database postgresql
        file: nome del file da cui prendere i dati da inserire nel database

    ritorna:
        str: errore di connessione al database postgresql
    """
    val = []
    val_new = []
    df = pd.read_excel(file) 

    create(config, df)

    for col_name in df.columns: 
        for col in df.itertuples():
            #perché voglio conoscere il valore delle righe? Lo posso ottenere semplicemente con 'df[col_name[0]]' dio maiale
            row_value = getattr(col, col_name, "N/A")
            val.append(row_value)

    for i in range(len(val)):
        value = val[i].replace("’", "")
        val_new.append(value)

    matrice = np.array(val_new).reshape(-1, len(df.columns))
    df2 = pd.DataFrame(matrice, columns=df.columns)
    insert(config, df2)

    try:
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute("select * from excelFile")
            value = cur.fetchone()
            return value
    except (psycopg2.DatabaseError, Exception) as error:
        return error


def searchSomething(config, company:str):
    """
    Individua e visualizza un risultato nella tabella dell'endpoint "\candidature"
    
    args:
        config:file di configurazione che permette la connessione con il database postgresql
        company:nome dell'azienda utilizzato per fare la ricerca

    returns:
        str: errore di connessione al database
    """
    try:
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute("select distinct * from job_application where company_name='{0}';", company)
            value = cur.fetchone()
            return value
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)
    return "hai cercato qualcosa"
