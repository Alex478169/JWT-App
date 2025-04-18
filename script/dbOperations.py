import psycopg2

def viewDataTable(config):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = psycopg2.cursor()
            cur.execute("SELECT * FROM job_application;")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insertJobApplication(config, appDate: str, contEmail: str, compName: str, jobTitle: str, jobUrl: str, resName: str):
     try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = psycopg2.cursor()
            cur.execute("INSERT INTO job_application(Application_Date, Contact_Email, Company_Name, Job_Title, Job_Url, Resume_Name) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');", appDate, contEmail, compName, jobTitle, jobUrl, resName)
            return conn
     except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print("Good job boy! you are connected to the database!")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
            print(error)

def showValues(config, column: str):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cur = conn.cursor()
            cur.execute(f"select {column} from job_application;")
            pippo = cur.fetchall()
            return pippo
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)