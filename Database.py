import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="Gandhi", password="Utestgandhi@2020",
                                  database="employee")
    cursor = con.cursor()
    cursor.execute("insert into student values('Eliza',104)")
    cursor.execute("insert into student values('Kattie',107);")
    cursor.execute("insert into student values('Kattie',107);")
    cursor.execute("Select * from student")

    for r in cursor:
        print(r[0], r[1])

    con.commit()
except:
    print("Connection UnSuccessful")
