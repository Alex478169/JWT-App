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

if __name__ == "__main__":
    config = load_config()
    connect(config)