def read_df(file: str)
     while True:
        try:
            df = pd.read_csv(file)
            break
        except Exception(FileNotFoundError) as error:
            print(error)
            break
        except Exception(ValueError) as error:
            print(error)
            break
        except Exception(ImportError) as error:
            print(error)
            break
        except Exception(PermissionError) as error:
            print(error)
            break
    return df

def create(colLength: int):
    colLength = Len
     match Len
        case 6:
            try:
                with psycopg2.connect(**config) as conn:
                    cur = conn.cursor()
                    cur.execute("CREATE TABLE excelFile({0} varchar(255), {1} varchar(255), {2} varchar(255), {3} varchar(255), {4} varchar(255))", df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])])
                    cur.commit()
                    print("è stata creata la tabella!")
            except (psycopg2.DatabaseError, Exception) as error:
                return str(error)

        case 7:
            try:
                with psycopg2.connect(**config) as conn:
                    cur = conn.cursor()
                    cur.execute("CREATE TABLE excelFile({0} varchar(255), {1} varchar(255), {2} varchar(255), {3} varchar(255), {4} varchar(255), {5} varchar(255))", df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])])
                    cur.commit()
                    print("è stata creata la tabella!")
            except (psycopg2.DatabaseError, Exception) as error:
                return str(error)

        case 8:
            try:
                with psycopg2.connect(**config) as conn:
                    cur = conn.cursor()
                    cur.execute("CREATE TABLE excelFile({0} varchar(255), {1} varchar(255), {2} varchar(255), {3} varchar(255), {4} varchar(255), {5} varchar(255), {6} varchar(255))", df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])], df[str(df.columns[6])])
                    cur.commit()
                    print("è stata creata la tabella!")
            except (psycopg2.DatabaseError, Exception) as error:
                return str(error)

        case 9:
            try:
                with psycopg2.connect(**config) as conn:
                    cur = conn.cursor()
                    cur.execute("CREATE TABLE excelFile({0} varchar(255), {1} varchar(255), {2} varchar(255), {3} varchar(255), {4} varchar(255), {5} varchar(255), {6} varchar(255), {7} varchar(255))", df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])], df[str(df.columns[6])], df[str(df.columns[7])])
                    cur.commit()
                    print("è stata creata la tabella!")
            except (psycopg2.DatabaseError, Exception) as error:
                return str(error)

        case 10:
            try:
                with psycopg2.connect(**config) as conn:cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}) VALUES ({5},{6},{7},{8},{9})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])])
                        
def insert(colLength: int):
    colLength = Len
    try:
        with psycopg2.connect(**config) as conn:
        match len(df.columns):
            case 6:
                try:
                    with psycopg2.connect(**config) as conn:
                        cur = conn.cursor()
                        for i in range(0, len(df[str(df.columns[0])]))
                            cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}) VALUES ({5},{6},{7},{8},{9})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])])
                            cur.commit()
                except (psycopg2.DatabaseError, Exception) as error:
                    return str(error)

            case 7:
                try:
                    with psycopg2.connect(**config) as conn:
                        cur = conn.cursor()
                        for i in range(0, len(df[str(df.columns[0])]))
                            cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}, {5}) values ({6}, {7}, {8}, {9}, {10}, {11})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), str(df.columns[5]), df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])])                        
                            cur.commit()
                except (psycopg2.DatabaseError, Exception) as error:
                    return str(error)

            case 8:
                try:
                    with psycopg2.connect(**config) as conn:
                        cur = conn.cursor()
                        for i in range(0, len(df[str(df.columns[0])]))
                            cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}, {5}, {6}) values ({7}, {8}, {9}, {10}, {11}, {12}, {13})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), str(df.columns[5]) ,df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])], df[str(df.columns[6])])
                            cur.commit()
                except (psycopg2.DatabaseError, Exception) as error:
                    return str(error)

            case 9:
                try:
                    with psycopg2.connect(**config) as conn:
                        cur = conn.cursor()
                        for i in range(0, len(df[str(df.columns[0])]))
                            cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) values ({8}, {9}, {10}, {11}, {12}, {13}, {14}, {15})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), str(df.columns[5]), str(df.columns[6]), str(df.columns[7]) , df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])], df[str(df.columns[6])], df[str(df.columns[7])])
                            cur.commit()
                except (psycopg2.DatabaseError, Exception) as error:
                    return str(error)

            case 10:
                try:
                    with psycopg2.connect(**config) as conn:
                        cur = conn.cursor()
                        for i in range(0, len(df[str(df.columns[0])]))
                            cur.execute("INSERT INTO excelFile({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) values ('{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', {17})", str(df.columns[0]), str(df.columns[1]), str(df.columns[2]), str(df.columns[3]), str(df.columns[4]), str(df.columns[5]), str(df.columns[6]), str(df.columns[7]), str(df.columns[8]) ,df[str(df.columns[0])], df[str(df.columns[1])], df[str(df.columns[2])], df[str(df.columns[3])], df[str(df.columns[4])], df[str(df.columns[5])], df[str(df.columns[6])], df[str(df.columns[7])], df[str(df.columns[8])])
                            cur.commit()
                except (psycopg2.DatabaseError, Exception) as error:
                    return str(error)
    except (psycopg2.DatabaseError, Exception) as error:
        return str(error)