from db import connectDB
import json

def verify_user(password, email):
    if password == None or email == None:
        return "Failure"
    conn = connectDB()
    cursor = conn.cursor()
    s = "select * from users where password='" + password + "' and email='" + email + "'"
    cursor.execute(s)
    result = cursor.fetchall()
    ans = []
    for i in result:
      ans.append(i)
    return json.dumps(ans)
def create_user(firstname, lastname, email, password):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("insert into users (firstname, lastname, email, password) values (%s, %s, %s, %s)", (firstname, lastname, email, password))
    conn.commit()
    if cursor.rowcount > 0:
        return "Sucess"
    else:
        return "Failure"
# print(login("jeff", "hubert.chen200@gmail.com"))

