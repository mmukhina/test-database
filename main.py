import psycopg2
from flask import Flask


app = Flask(__name__)

@app.route('/')
def main():
    host = "ec2-3-211-6-217.compute-1.amazonaws.com"
    name = "d9ig9ca9682pc6"
    user = "ijyzomfmfgkqla"
    password = "d1d0923a4e5d9727ad012bbe8f412289b305b0415d129577b3310c3929af7933"

    conn = psycopg2.connect(dbname = name, user = user, password = password, host = host)

    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    result = str((cur.fetchall())[0][0])

    cur.close()

    conn.close()
    print(result)
    
    return result

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




