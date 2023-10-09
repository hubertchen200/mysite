
# # A very simple Flask Hello World app for you to get started with...
import mysql.connector

mysql_connection = None

def connectDB():
    global mysql_connection
    if mysql_connection != None:
        return mysql_connection

    config = {
      'user': 'hubertchen200',
      'password': '1qaz)P:?',
      'host': 'hubertchen200.mysql.pythonanywhere-services.com',
      'database': 'hubertchen200$db1',
      'raise_on_warnings': True
    }
    try:
        mysql_connection = mysql.connector.connect(**config)
        print('My SQL Connection created successfully!')
    except:
        mysql_connection = None
        print('Connect to MySQL failure!')
    return mysql_connection

# def insert_student(stu_id, stu_name):
#     global mysql_connection
#     print("tes")

#     mysql_insert_query = f"""INSERT INTO students (stu_id, stud_name)
#                           VALUES
#                           ('{stu_id}', '{stu_name}')"""
#     print(mysql_insert_query)
#     try:
#         print(mysql_connection)
#         cursor = mysql_connection.cursor()
#         cursor.execute(mysql_insert_query)
#         mysql_connection.commit()
#         res = "Record inserted successfully into student table: " + str(cursor.rowcount)
#         cursor.close()
#         return res
#     except:
#         return "error!"

# # connectDB()
# # print(insert_student("1","hubert"))
# def connectDB():
#     config = {
#         'user': 'hubertchen200',
#         'password': '1qaz)P:?',
#         'host': 'hubertchen200.mysql.pythonanywhere-services.com',
#         'database': 'hubertchen200$db1',
#         'raise_on_warnings': True
#     }
#     print(*config)
#     return mysql.connector.connect(**config)

# def get_users():
#     conn = connectDB()
#     s = "select * from users"
#     cursor = conn.cursor()
#     cursor.execute(s)
#     result = cursor.fetchall()
#     for i in result:
#         print(i)
# get_users()

# connectDB()
