import psycopg2
from DBcredential import Token

with psycopg2.connect(
  host=Token.get("hostname"),
  user=Token.get("username"),
  password=Token.get("pwd"),
  database=Token.get("database"),
  port=Token.get("port_id")
) as conn:
    
    with conn.cursor() as curs:
        curs.execute('''CREATE TABLE IF NOT EXISTS employee(
            EmployeeID int,
            Name varchar(255),
            Email varchar(255));
        ''')

        curs.execute('''
        INSERT INTO employee (EmployeeID, Name, Email)
            VALUES (101, 'Mark', 'mark@company.com'),
                (102, 'Robert', 'robert@company.com'),
                (103, 'Spencer', 'spencer@company.com');
        ''')

        delete_script = '''delete from employee where Name = %s'''
        curs.execute(delete_script,("Mark",))
        conn.commit()