import psycopg2
import config as cfg


def conn_pgsql():
    try:
        conn = psycopg2.connect(host=cfg.PGSQL_CONFIG['host'],
                                database=cfg.PGSQL_CONFIG['db_name'],
                                user=cfg.PGSQL_CONFIG['user'],
                                password=cfg.PGSQL_CONFIG['password'])
    except:
        print("Unable to connect Postgres DB")
    return conn


def create_table(connection, sql_query):
    try:
        cur = connection.cursor()
        cur.execute(sql_query)
        print("Created Postgres table")
    except psycopg2.DatabaseError as e:
        print(e)


def insert_data(connection, sql_query):
    try:
        cur = connection.cursor()
        cur.execute(sql_query)
        connection.commit()
        print("Data inserted successfully")
    except psycopg2.DatabaseError as e:
        if connection:
            connection.rollback()
            print(e)


def insert_multi_rows(connection, sql_query, row_list):
    try:
        cur = connection.cursor()
        cur.executemany(sql_query, row_list)
        connection.commit()
        print("Multiple Row Data inserted successfully")
    except psycopg2.DatabaseError as e:
        if connection:
            connection.rollback()
            print(e)


def select_data(connection, sql_query):
    try:
        cur = connection.cursor()
        cur.execute(sql_query)
        result_set = cur.fetchall()
        # Following statement will return table data as list of tuples
        return result_set
    except psycopg2.DatabaseError as e:
        if connection:
            print(e)


def drop_table(connection, sql_query):
    try:
        cur = connection.cursor()
        cur.execute(sql_query)
        connection.commit()
        print("Dropped Postgres table")
    except psycopg2.DatabaseError as e:
        if connection:
            print(e)


def main():
    con = conn_pgsql()

    create_query = "CREATE TABLE employees(emp_id INTEGER PRIMARY KEY, emp_name VARCHAR(20))"
    create_table(con, create_query)

    insert_query1 = "INSERT INTO employees VALUES(1,'Name1')"
    insert_query2 = "INSERT INTO employees VALUES(2,'Name2')"
    insert_query3 = "INSERT INTO employees VALUES(3,'Name3')"
    insert_query4 = "INSERT INTO employees VALUES(4,'Name4')"
    insert_data(con, insert_query1)
    insert_data(con, insert_query2)
    insert_data(con, insert_query3)
    insert_data(con, insert_query4)

    rows = [(5, 'Name5'),
            (6, 'Name6'),
            (7, 'Name7'),
            (8, 'Name8')]
    insert_multi_query = "INSERT INTO employees VALUES(%s, %s)"
    insert_multi_rows(con, insert_multi_query, rows)

    select_query = "SELECT * from employees"
    res = select_data(con, select_query)

    drop_query = "DROP TABLE employees"
    #drop_table(con, drop_query)

    con.close()

    print(res)
    print("Displaying each row")
    for row in res:
        print(row)


if __name__ == "__main__":
    # calling the main function
    main()

