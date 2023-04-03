import psycopg2
try:
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='swasthika', host='localhost', port= '5432'
)
except Exception as error:
    print(error)
cur = conn.cursor()
conn.commit()

def postgres_test():

    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='swasthika' connect_timeout=1 ")
        #conn.close()
        return True
    except:
        return False  
print(postgres_test)
create_script = ''' CREATE TABLE IF NOT EXISTS field (
                                    id      int PRIMARY KEY,
                                    first_name    varchar(40) NOT NULL,
                                    last_name    varchar(40) NOT NULL,
                                    mail   varchar(40) NOT NULL,
                                    phone    int NOT NULL,
                                    dob   date NOT NULL,
                                    gender    varchar(40) NOT NULL,
                                    adress1    varchar(40) NOT NULL,
                                    address2    varchar(40) NOT NULL,
                                    city    varchar(40) NOT NULL,
                                    state    varchar(40) NOT NULL,
                                    postal_code    varchar(40) NOT NULL,
                                    country  int,
                                    '''
cur.execute(create_script)

