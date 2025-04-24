import psycopg2
import pandas as pd

def viewDataTable(config, table: str):
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
     try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = psycopg2.cursor()
            cur.execute("INSERT INTO job_application(Application_Date, Contact_Email, Company_Name, Job_Title, Job_Url, Resume_Name) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');", appDate, contEmail, compName, jobTitle, jobUrl, resName)
            return conn
     except (psycopg2.DatabaseError, Exception) as error:
        return(error)

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            return "Good job boy! you are connected to the database!"
    except (psycopg2.DatabaseError, Exception) as error:
            return str(error)

def showValues(config, column: str):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute(f"select {column} from job_application;")
            rows = cur.fetchall()
            return rows
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def insertValues(config, username:str, password:str):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            values = viewDataTable(config, "users")
            for row in values:
                if username in row and password in row :
                    return "l'utente esiste già, attaccati"
                else:
                    cur.execute(f"INSERT INTO users(id, username, password) VALUES ('%s', '%s');", username, password)
                    conn.commit()
                    return "hai inserito un nuovo utente"
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def compareValues(config, username:str, password:str):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            #creazione di un cursore
            cur = conn.cursor()

            #esecuzione di una query che trova la password dell'utente richiesto
            cur.execute(f"SELECT password FROM users WHERE username='{username}'")
            #e prende il valore
            value = cur.fetchone()
            #per qualche strano motivo non mi stampa il valore della query
            print(value)
               
            if password in value[0]:
                return True
            else:
                return False

    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)

def fromCSVToSQL(config, file: str, table:str):
    df = pd.read_csv(file)
    #modifica il contenuto di una cella su una riga esatta (tipo query di UPDATE)
    df.loc[df["Application Date"] == "9/9/24, 8:21 AM", "Company Name"] = "Tecne - Gruppo Autostrade per Italia"
    df.to_csv(file)
    insertQueries=[]

        #itera sulle righe
    for _,row in df.iterrows():
        application_date = row["Application Date"].replace("'", "''")
        contact_email = row["Contact Email"].replace("'", "''")
        company_name = row["Company Name"].replace("'", "''")
        job_title = row["Job Title"].replace("'", "''")
        job_url = row["Job Url"].replace("'", "''")
        resume_name = row["Resume Name"].replace("'", "''")
        print(application_date)

        sqlInsert = f"INSERT INTO {table}(application_date, contact_email, company_name, job_title, job_url, resume_name) VALUES ('{application_date}', '{contact_email}', '{company_name}', '{job_title}', '{job_url}', '{resume_name}');"
        insertQueries.append(sqlInsert)
        try:
            with psycopg2.connect(**config) as conn:
                cur = conn.cursor()
                for sql in insertQueries:    
                    cur.execute(sql)
                    conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            return str(error)
    return "tutto è andato buon fine"

def searchSomething(config, company:str):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            #creazione di un cursore
            cur = conn.cursor()

            #esecuzione di una query che trova la password dell'utente richiesto
            cur.execute(f"select distinct * from job_application where company_name='{company}';")
            #e prende il valore
            value = cur.fetchone()
            print(value)
            return value
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)
    return "hai cercato qualcosa"