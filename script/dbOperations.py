import psycopg2

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
            cur.execute("select %s from job_application;", column)
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